from src.services.clientes_service import (cadastrar_cliente, listar_clientes) 
import psycopg


def tela_cadastrar_cliente():
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