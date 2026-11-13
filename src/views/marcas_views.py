"""Telas de cadastro, consulta, atualização e exclusão de marcas."""

import psycopg

from src.services.marcas_service import (
    atualizar_marca,
    buscar_marca,
    cadastrar_marca,
    excluir_marca,
    listar_marcas,
)

from src.utils.terminal import limpar_terminal, pausar_terminal


def tela_cadastrar_marca():
    """Solicita o nome da marca e apresenta o resultado do cadastro."""
    limpar_terminal()
    print('\n--- Cadastrar marca ---')

    try:
        nome = input('Nome da marca: ')
        cadastrar_marca(nome)

        print('Marca cadastrada com sucesso!')

    except ValueError as erro:
        print(erro)

    except psycopg.Error:
        print('Não foi possível cadastrar a marca.')


def tela_listar_marcas():
    """Mostra os IDs e nomes das marcas cadastradas."""
    limpar_terminal()
    print('\n--- Marcas cadastradas ---')

    try:
        marcas = listar_marcas()

        if not marcas:
            print('Nenhuma marca cadastrada.')
            return

        for marca in marcas:
            print(f"{marca['id_marca']} - {marca['nome']}")

    except psycopg.Error:
        print('Não foi possível listar as marcas.')


def tela_buscar_marca():
    """Solicita o ID e apresenta a marca encontrada."""
    limpar_terminal()
    print('\n--- Buscar marca ---')

    try:
        id_marca = input('ID da marca: ')
        marca = buscar_marca(id_marca)

        print(f"ID: {marca['id_marca']}")
        print(f"Nome: {marca['nome']}")

    except ValueError as erro:
        print(erro)

    except psycopg.Error:
        print('Não foi possível buscar a marca.')


def tela_atualizar_marca():
    """Permite alterar o nome de uma marca existente."""
    limpar_terminal()
    print('\n--- Atualizar marca ---')

    try:
        id_marca = input('ID da marca: ')
        marca = buscar_marca(id_marca)

        print(f"Nome atual: {marca['nome']}")
        nome = input('Novo nome: ').strip()

        if not nome or nome == marca['nome']:
            print('Nenhuma alteração realizada.')
            return

        atualizar_marca(id_marca, nome)

        print('Marca atualizada com sucesso!')

    except ValueError as erro:
        print(erro)

    except psycopg.Error:
        print('Não foi possível atualizar a marca.')


def tela_excluir_marca():
    """Confirma a exclusão da marca e apresenta possíveis impedimentos."""
    limpar_terminal()
    print('\n--- Excluir marca ---')

    try:
        id_marca = input('ID da marca: ')
        marca = buscar_marca(id_marca)

        print(f"Marca: {marca['nome']}")

        confirmacao = input('Deseja excluir esta marca? (s/n): ').strip().lower()

        if confirmacao != 's':
            print('Exclusão cancelada.')
            return

        excluir_marca(id_marca)

        print('Marca excluída com sucesso!')

    except ValueError as erro:
        print(erro)

    except psycopg.Error:
        print('Não foi possível excluir a marca.')


def menu_marcas():
    """Exibe as opções de marcas e encaminha para a tela escolhida."""
    while True:
        limpar_terminal()
        print('\n--- Marcas ---')
        print('1 - Cadastrar marca')
        print('2 - Listar marcas')
        print('3 - Buscar marca por ID')
        print('4 - Atualizar marca')
        print('5 - Excluir marca')
        print('0 - Voltar')

        opcao = input('Opção: ').strip()

        if opcao == '1':
            tela_cadastrar_marca()

        elif opcao == '2':
            tela_listar_marcas()

        elif opcao == '3':
            tela_buscar_marca()

        elif opcao == '4':
            tela_atualizar_marca()

        elif opcao == '5':
            tela_excluir_marca()

        elif opcao == '0':
            return

        else:
            print('Opção inválida.')

        pausar_terminal()
