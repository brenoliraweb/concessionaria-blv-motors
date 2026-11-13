from src.utils.terminal import limpar_terminal, pausar_terminal
from src.services.clientes_service import (cadastrar_cliente, listar_clientes, listar_cliente_por_id, atualizar_cliente, excluir_cliente, buscar_cliente_por_cpf) 
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
    except psycopg.Error:
        print('Não foi possível cadastrar o cliente.')    

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

def tela_buscar_cliente_por_id():
    limpar_terminal()
    print('\n--- Buscar cliente por ID ---')

    try:
        id_cliente = input('ID do cliente: ')
        cliente = listar_cliente_por_id(id_cliente)

        print(f"\nID: {cliente['id_cliente']}")
        print(f"Nome: {cliente['nome']}")
        print(f"CPF: {cliente['cpf']}")
        print(f"Telefone: {cliente['telefone']}")
        print(f"E-mail: {cliente['email'] or 'Não informado'}")

    except ValueError as erro:
        print(erro)

    except psycopg.Error:
        print('Não foi possível buscar o cliente.')
        
def tela_buscar_cliente_por_cpf():
    limpar_terminal()
    print('\n--- Buscar cliente por CPF ---')

    try:
        cpf = input('CPF do cliente: ')
        cliente = buscar_cliente_por_cpf(cpf)

        print(f"\nID: {cliente['id_cliente']}")
        print(f"Nome: {cliente['nome']}")
        print(f"CPF: {cliente['cpf']}")
        print(f"Telefone: {cliente['telefone']}")
        print(f"E-mail: {cliente['email'] or 'Não informado'}")

    except ValueError as erro:
        print(erro)

    except psycopg.Error:
        print('Não foi possível buscar o cliente.')

def tela_atualizar_cliente():
    limpar_terminal()
    print('\n--- Atualizar cliente ---')

    try:
        id_cliente = input('ID do cliente: ')
        cliente = listar_cliente_por_id(id_cliente)

        nome = cliente['nome']
        cpf = cliente['cpf']
        telefone = cliente['telefone']
        email = cliente['email']

        print(f'\nCliente: {nome}')
        print('\nO que deseja atualizar?')
        print('1 - Nome')
        print('2 - CPF')
        print('3 - Telefone')
        print('4 - E-mail')
        print('5 - Todos os dados')
        print('0 - Voltar')

        opcao = input('Opção: ').strip()

        if opcao == '0':
            return

        if opcao not in ('1', '2', '3', '4', '5'):
            print('Opção inválida.')
            return

        print('\nPressione Enter para manter o valor atual.')

        if opcao in ('1', '5'):
            nome = input(f'Nome: ').strip() or nome

        if opcao in ('2', '5'):
            cpf = input(f'CPF: ').strip() or cpf

        if opcao in ('3', '5'):
            telefone = input(f'Telefone: ').strip() or telefone

        if opcao in ('4', '5'):
            novo_email = input(
                f'E-mail(- para remover): '
            ).strip()

            if novo_email == '-':
                email = None
            elif novo_email:
                email = novo_email

        atualizar_cliente(id_cliente, nome, cpf, telefone, email)

        print('Cliente atualizado com sucesso!')

    except ValueError as erro:
        print(erro)

    except psycopg.Error:
        print('Não foi possível atualizar o cliente.')
        
def tela_excluir_cliente(funcionario):
    limpar_terminal()
    print('\n--- Excluir cliente ---')

    try:
        id_cliente = input('ID do cliente: ')
        cliente = listar_cliente_por_id(id_cliente)

        print(f"\nNome: {cliente['nome']}")
        print(f"CPF: {cliente['cpf']}")

        confirmacao = input('\nDeseja excluir este cliente? (s/n): ').strip().lower()

        if confirmacao != 's':
            print('Exclusão cancelada.')
            return

        excluir_cliente(id_cliente, funcionario)
        print('Cliente excluído com sucesso!')

    except (ValueError, PermissionError) as erro:
        print(erro)

    except psycopg.Error:
        print('Não foi possível excluir o cliente.')

def menu_clientes(funcionario):
    """
        Exibe o menu de clientes e direciona para as telas disponíveis.
    """
    while True:
        limpar_terminal()
        print('\n--- Clientes ---')
        print('1 - Cadastrar cliente')
        print('2 - Listar clientes')
        print('3 - Buscar cliente pelo id')
        print('4 - Buscar cliente pelo cpf')
        print('5 - Atualizar cliente')
        print('6 - Excluir cliente')
        print('0 - Voltar')

        opcao = input('Opção: ').strip()

        if opcao == '1':
            tela_cadastrar_cliente()
        elif opcao == '2':
            tela_listar_clientes()
        elif opcao == '3':
            tela_buscar_cliente_por_id()
        elif opcao == '4':
            tela_buscar_cliente_por_cpf()
        elif opcao == '5':
            tela_atualizar_cliente()
        elif opcao == '6':
            tela_excluir_cliente(funcionario)
        elif opcao == '0':
            return
        else:
            print('Opção inválida.')

        pausar_terminal()
