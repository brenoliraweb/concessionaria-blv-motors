from src.utils.terminal import limpar_terminal, pausar_terminal
from src.views.clientes_views import menu_clientes
from src.views.funcionarios_views import menu_funcionarios


def menu_admin(funcionario=None):
    """
        Exibe o painel do administrador e direciona para os menus de clientes e funcionários.
    """
    while True:
        limpar_terminal()
        if funcionario:
            print(f"Bem-vindo(a), {funcionario['nome']}!")
        print('\n--- BLV Motors | Administrador ---')
        print('1 - Clientes')
        print('2 - Funcionários')
        print('0 - Sair da conta')

        opcao = input('Opção: ').strip()

        if opcao == '1':
            menu_clientes()
        elif opcao == '2':
            menu_funcionarios()
        elif opcao == '0':
            return
        else:
            print('Opção inválida.')
            pausar_terminal()
