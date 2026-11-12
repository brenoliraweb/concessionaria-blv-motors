# Inclui a raiz do projeto ao executar este arquivo diretamente.
if __package__ in (None, ''):
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.views.auth_views import auth_menu
from src.views.principal_views import menu_principal

def main():
    """
        Inicia o sistema e controla o ciclo de login e acesso aos painéis.
    """
    while True:
        funcionario = auth_menu()
        if funcionario is None:
            return
        menu_principal(funcionario)


if __name__ == '__main__':
    main()
