from src.utils.terminal import limpar_terminal, pausar_terminal
from src.views.vendas.vendas_views import tela_registrar_venda
from src.views.clientes.clientes_views import (
    tela_atualizar_cliente,
    tela_buscar_cliente_por_cpf,
    tela_cadastrar_cliente,
)

def menu_vendedor(funcionario=None):
    """
        Exibe o atendimento ao cliente e as opções de veículos e vendas pendentes.
    """

    while True:
        limpar_terminal()
        if funcionario:
            print(f"Bem-vindo(a), {funcionario['nome']}!")

        print('\n--- BLV Motors | Vendedor ---')
        print('1 - Cadastrar cliente')
        print('2 - Atualizar cliente')
        print('3 - Buscar cliente pelo cpf')
        print('4 - Consultar veículos disponíveis')
        print('5 - Registrar venda')
        print('0 - Sair da conta')

        opcao = input('Opção: ').strip()

        if opcao == '1':
            tela_cadastrar_cliente()

        elif opcao == '2':
            tela_atualizar_cliente()

        elif opcao == '3':
            tela_buscar_cliente_por_cpf()

        elif opcao == '4':
            print('Em desenvolvimento.')

        elif opcao == '5':
            tela_registrar_venda(funcionario)

        elif opcao == '0':
            return
        
        else:
            print('Opção inválida.')

        pausar_terminal()