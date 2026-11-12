import os
import sys


def limpar_terminal():
    """
        Limpa a tela do terminal conforme o sistema operacional quando a saída é interativa.
    """
    if sys.stdout.isatty():
        os.system('cls' if os.name == 'nt' else 'clear')


def pausar_terminal():
    """
        Aguarda Enter para manter as mensagens visíveis antes de trocar de tela.
    """
    input('\nPressione Enter para continuar...')
