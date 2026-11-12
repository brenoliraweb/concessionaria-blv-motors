from src.utils.terminal import limpar_terminal, pausar_terminal
from src.views.clientes_views import tela_cadastrar_cliente


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
        print('2 - Buscar cliente pelo nome')
        print('3 - Registrar venda')
        print('0 - Sair da conta')

        opcao = input('Opção: ').strip()

        if opcao == '1':
            tela_cadastrar_cliente()
        elif opcao in ('2', '3'):
            print('Em desenvolvimento.')
        elif opcao == '0':
            return
        else:
            print('Opção inválida.')

        pausar_terminal()
