import psycopg

from src.utils.terminal import limpar_terminal, pausar_terminal
from src.services.funcionarios_service import (
    cadastrar_funcionario,
    listar_funcionarios,
    listar_funcionario_por_id,
    atualizar_funcionario,
    atualizar_login_funcionario,
    deletar_funcionario,
)


def tela_cadastrar_funcionario():
    """Solicita os dados e apresenta o resultado do cadastro do funcionário."""
    limpar_terminal()
    print('\n--- Cadastrar funcionário ---')

    try:
        nome = input('Digite o nome: ')
        cpf = input('Digite o CPF: ')
        telefone = input('Digite o telefone: ')
        cargo = input('Digite o cargo (admin/vendedor): ')
        login = input('Digite o login: ')
        senha = input('Digite a senha: ')

        cadastrar_funcionario(nome, cpf, telefone, cargo, login, senha)
        print('Funcionário cadastrado com sucesso!')

    except ValueError as erro:
        print(erro)
    except psycopg.Error:
        print('Não foi possível cadastrar o funcionário.')


def tela_listar_funcionarios():
    """Consulta e exibe os funcionários cadastrados no sistema."""
    limpar_terminal()
    print('\n--- Funcionários cadastrados ---')

    try:
        funcionarios = listar_funcionarios()

        if not funcionarios:
            print('Nenhum funcionário cadastrado.')
            return

        for funcionario in funcionarios:
            print(f"\nID: {funcionario['id_funcionario']}")
            print(f"Nome: {funcionario['nome']}")
            print(f"CPF: {funcionario['cpf']}")
            print(f"Telefone: {funcionario['telefone']}")
            print(f"Cargo: {funcionario['cargo']}")

    except psycopg.Error:
        print('Não foi possível listar os funcionários.')


def tela_buscar_funcionario_por_id():
    limpar_terminal()
    print('\n--- Buscar funcionário por ID ---')

    try:
        id_funcionario = input('ID do funcionário: ')
        funcionario = listar_funcionario_por_id(id_funcionario)

        print(f"\nID: {funcionario['id_funcionario']}")
        print(f"Nome: {funcionario['nome']}")
        print(f"CPF: {funcionario['cpf']}")
        print(f"Telefone: {funcionario['telefone']}")
        print(f"Cargo: {funcionario['cargo']}")
        print(f"Login: {funcionario['login']}")

    except ValueError as erro:
        print(erro)
    except psycopg.Error:
        print('Não foi possível buscar o funcionário.')


def tela_atualizar_funcionario():
    limpar_terminal()
    print('\n--- Atualizar funcionário ---')

    try:
        id_funcionario = input('ID do funcionário: ')
        funcionario = listar_funcionario_por_id(id_funcionario)

        nome = funcionario['nome']
        cpf = funcionario['cpf']
        telefone = funcionario['telefone']
        cargo = funcionario['cargo']

        print(f'\nFuncionário: {nome}')
        print('\nO que deseja atualizar?')
        print('1 - Nome')
        print('2 - CPF')
        print('3 - Telefone')
        print('4 - Cargo')
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
            nome = input('Nome: ').strip() or nome
        if opcao in ('2', '5'):
            cpf = input('CPF: ').strip() or cpf
        if opcao in ('3', '5'):
            telefone = input('Telefone: ').strip() or telefone
        if opcao in ('4', '5'):
            cargo = input('Cargo (admin/vendedor): ').strip() or cargo

        atualizar_funcionario(nome, cpf, telefone, cargo, id_funcionario)
        print('Funcionário atualizado com sucesso!')

    except ValueError as erro:
        print(erro)
    except psycopg.Error:
        print('Não foi possível atualizar o funcionário.')


def tela_atualizar_login_funcionario():
    limpar_terminal()
    print('\n--- Alterar login e senha ---')

    try:
        id_funcionario = input('ID do funcionário: ')
        funcionario = listar_funcionario_por_id(id_funcionario)

        print(f"\nFuncionário: {funcionario['nome']}")
        print(f"Login atual: {funcionario['login']}")
        login = input('Novo login (Enter para manter o atual): ').strip()
        login = login or funcionario['login']
        senha = input('Nova senha: ')

        atualizar_login_funcionario(login, senha, id_funcionario)
        print('Login e senha atualizados com sucesso!')

    except ValueError as erro:
        print(erro)
    except psycopg.Error:
        print('Não foi possível atualizar o login e a senha do funcionário.')


def tela_excluir_funcionario():
    limpar_terminal()
    print('\n--- Excluir funcionário ---')

    try:
        id_funcionario = input('ID do funcionário: ')
        funcionario = listar_funcionario_por_id(id_funcionario)

        print(f"\nNome: {funcionario['nome']}")
        print(f"CPF: {funcionario['cpf']}")
        confirmacao = input('\nDeseja excluir este funcionário? (s/n): ').strip().lower()

        if confirmacao != 's':
            print('Exclusão cancelada.')
            return

        deletar_funcionario(id_funcionario)
        print('Funcionário excluído com sucesso!')

    except ValueError as erro:
        print(erro)
    except psycopg.Error:
        print('Não foi possível excluir o funcionário.')


def tela_elevar_cargo_funcionario():
    limpar_terminal()
    print('\n--- Elevar cargo para administrador ---')

    try:
        id_funcionario = input('ID do funcionário: ')
        funcionario = listar_funcionario_por_id(id_funcionario)

        print(f"\nNome: {funcionario['nome']}")
        print(f"Cargo atual: {funcionario['cargo']}")

        if funcionario['cargo'] == 'admin':
            print('O funcionário já é administrador.')
            return

        confirmacao = input('\nDeseja promover este funcionário a administrador? (s/n): ').strip().lower()

        if confirmacao != 's':
            print('Promoção cancelada.')
            return

        atualizar_funcionario(
            funcionario['nome'], funcionario['cpf'], funcionario['telefone'],
            'admin', id_funcionario,
        )
        print('Funcionário promovido a administrador com sucesso!')

    except ValueError as erro:
        print(erro)
    except psycopg.Error:
        print('Não foi possível promover o funcionário a administrador.')


def menu_funcionarios():
    """
        Exibe o menu de funcionários e direciona para as telas disponíveis.
    """
    while True:
        limpar_terminal()
        print('\n--- Funcionários ---')
        print('1 - Cadastrar funcionário')
        print('2 - Listar funcionários')
        print('3 - Buscar funcionário por ID')
        print('4 - Atualizar funcionário')
        print('5 - Alterar login e senha')
        print('6 - Excluir funcionário')
        print('7 - Elevar cargo para administrador')
        print('0 - Voltar')

        opcao = input('Opção: ').strip()

        if opcao == '1':
            tela_cadastrar_funcionario()
        elif opcao == '2':
            tela_listar_funcionarios()
        elif opcao == '3':
            tela_buscar_funcionario_por_id()
        elif opcao == '4':
            tela_atualizar_funcionario()
        elif opcao == '5':
            tela_atualizar_login_funcionario()
        elif opcao == '6':
            tela_excluir_funcionario()
        elif opcao == '7':
            tela_elevar_cargo_funcionario()
        elif opcao == '0':
            return
        else:
            print('Opção inválida.')

        pausar_terminal()


def primeiro_funcionario():
    """
        Solicita os dados e cadastra um administrador quando chamada manualmente na configuração inicial.
    """
    limpar_terminal()
    print('\n--- Cadastro inicial de administrador ---')
    nome = input('Nome: ')
    cpf = input('CPF: ')
    telefone = input('Telefone: ')
    login = input('Login: ')
    senha = input('Senha: ')

    try:
        cadastrar_funcionario(nome, cpf, telefone, 'admin', login, senha)
        print('Funcionário cadastrado com sucesso!')
    except ValueError as erro:
        print(erro)
    except psycopg.Error:
        print('Não foi possível cadastrar o administrador inicial.')

    pausar_terminal()
