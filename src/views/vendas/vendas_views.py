import psycopg

from src.services.clientes.clientes_service import listar_cliente_por_id
from src.services.veiculos.veiculos_service import buscar_veiculo
from src.services.vendas.vendas_service import registrar_venda
from src.utils.terminal import limpar_terminal, pausar_terminal

def tela_registrar_venda(funcionario):
    limpar_terminal()
    print('\n--- Registrar venda ---')

    try:
        id_cliente = input('ID do cliente: ')
        cliente = listar_cliente_por_id(id_cliente)
        print(f"Cliente: {cliente['nome']}")

        id_veiculo = input('ID do veículo: ')
        veiculo = buscar_veiculo(id_veiculo)
        print(f"Veículo: {veiculo['marca']} {veiculo['modelo']}")
        print(f"Chassi: {veiculo['chassi']}")
        print(f"Preço anunciado: R$ {veiculo['preco_anunciado']:.2f}")

        valor_venda = input('Valor negociado: ')

        print('\nForma de pagamento')
        print('1 - Dinheiro')
        print('2 - Pix')
        print('3 - Cartão')
        print('4 - Financiamento')

        opcao = input('Opção: ').strip()
        formas_pagamento = {
            '1': 'dinheiro',
            '2': 'pix',
            '3': 'cartao',
            '4': 'financiamento',
        }
        forma_pagamento = formas_pagamento.get(opcao)

        if forma_pagamento is None:
            print('Forma de pagamento inválida.')
            return

        confirmacao = input('\nConfirma o registro da venda? (s/n): ').strip().lower()

        if confirmacao != 's':
            print('Registro cancelado.')
            return

        registrar_venda(id_cliente, funcionario['id_funcionario'], id_veiculo,valor_venda, forma_pagamento)
        print('Venda registrada com sucesso!')

    except ValueError as erro:
        print(erro)

    except psycopg.Error:
        print('Não foi possível registrar a venda.')
          
def menu_vendas(funcionario):
    while True:
        limpar_terminal()
        print('\n--- Vendas ---')
        print('1 - Registrar venda')
        print('0 - Voltar')

        opcao = input('Opção: ').strip()

        if opcao == '1':
            tela_registrar_venda(funcionario)
        elif opcao == '0':
            return
        else:
            print('Opção inválida.')

        pausar_terminal()
        
