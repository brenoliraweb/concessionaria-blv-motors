"""Tela de login e encerramento do sistema."""

import psycopg

from src.services.funcionarios_service import autenticar_funcionario
from src.utils.terminal import limpar_terminal, pausar_terminal


def auth_menu():
    """
    Exibe o login e retorna o funcionário autenticado ou None ao encerrar o
    sistema.
    """
    while True:
        limpar_terminal()
        print('\n=== BLV Motors ===\n')
        print('[1] - Entrar')
        print('[0] - Encerrar')

        opcao = input('Escolha uma opção: ').strip()

        if opcao == '0':
            print('Encerrando sistema...')
            return None

        if opcao != '1':
            print('Opção inválida.')
            pausar_terminal()
            continue

        login = input('\nLogin: ')
        senha = input('Senha: ')

        try:
            funcionario = autenticar_funcionario(login, senha)
        except ValueError as erro:
            print(erro)
            pausar_terminal()
        except psycopg.Error:
            print('Não foi possível entrar. Verifique a conexão com o banco de dados.')
            pausar_terminal()
        else:
            return funcionario
