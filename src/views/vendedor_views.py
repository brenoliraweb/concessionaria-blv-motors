from src.utils.terminal import limpar_terminal, pausar_terminal
from src.views.clientes_views import tela_cadastrar_cliente, tela_atualizar_cliente


def menu_vendedor(funcionario=None):
    """
        Exibe o painel do vendedor, com cadastro de cliente e opções de busca e venda em desenvolvimento.
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
        elif opcao in ('3', '4', '5'):
            print('Em desenvolvimento.')
        elif opcao == '0':
            return
        else:
            print('Opção inválida.')

        pausar_terminal()
