from src.utils.terminal import pausar_terminal
from src.views.admin_views import menu_admin
from src.views.vendedor_views import menu_vendedor


def menu_principal(funcionario):
    """
        Encaminha o funcionário autenticado ao painel correspondente ao seu cargo.
    """
    cargo = funcionario.get('cargo')

    if cargo == 'admin':
        menu_admin(funcionario)
    elif cargo == 'vendedor':
        menu_vendedor(funcionario)
    else:
        print('Acesso negado: cargo sem permissão para acessar o sistema.')
        pausar_terminal()
