from src.utils.terminal import limpar_terminal, pausar_terminal
from src.services.clientes_service import (cadastrar_cliente, listar_clientes) 
import psycopg


def tela_cadastrar_cliente():
    """
        Solicita os dados do cliente e apresenta o resultado do cadastro.
    """
    limpar_terminal()
    print('\n--- Cadastrar cliente ---')
    try:
        nome = input('Digite o nome: ')
        cpf = input('Digite o CPF: ')
        telefone = input('Digite o telefone: ')
        email = input('Digite o e-mail (opcional): ')

        cadastrar_cliente(nome, cpf, telefone, email)

        print('Cliente cadastrado com sucesso!')

    except ValueError as erro:
        print(erro)

def tela_listar_clientes():
    """
        Consulta e exibe os clientes cadastrados no sistema.
    """
    limpar_terminal()
    print('\n--- Clientes cadastrados ---')

    try:
        clientes = listar_clientes()

        if not clientes:
            print('Nenhum cliente cadastrado.')
            return

        for cliente in clientes:
            print(f"\nID: {cliente['id_cliente']}")
            print(f"Nome: {cliente['nome']}")
            print(f"CPF: {cliente['cpf']}")
            print(f"Telefone: {cliente['telefone']}")
            print(f"E-mail: {cliente['email'] or 'Não informado'}")

    except psycopg.Error:
        print('Não foi possível listar os clientes.')


def menu_clientes():
    """
        Exibe o menu de clientes e direciona para as telas disponíveis.
    """
    while True:
        limpar_terminal()
        print('\n--- Clientes ---')
        print('1 - Cadastrar cliente')
        print('2 - Listar clientes')
        print('3 - Buscar cliente')
        print('4 - Atualizar cliente')
        print('5 - Excluir cliente')
        print('0 - Voltar')

        opcao = input('Opção: ').strip()

        if opcao == '1':
            tela_cadastrar_cliente()
        elif opcao == '2':
            tela_listar_clientes()
        elif opcao in ('3', '4', '5'):
            print('Em desenvolvimento.')
        elif opcao == '0':
            return
        else:
            print('Opção inválida.')

        pausar_terminal()
