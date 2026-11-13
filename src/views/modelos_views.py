"""Telas de gerenciamento dos modelos vinculados às marcas."""

import psycopg

from src.services.marcas_service import listar_marcas
from src.services.modelos_service import (
    atualizar_modelo,
    buscar_modelo,
    cadastrar_modelo,
    excluir_modelo,
    exigir_administrador,
    listar_modelos,
)
from src.utils.terminal import limpar_terminal, pausar_terminal


def _exibir_modelo(modelo):
    """Apresenta o modelo com os dados da marca correspondente."""
    print(f"\nID: {modelo['id_modelo']}")
    print(f"Marca: {modelo['marca']} (ID: {modelo['id_marca']})")
    print(f"Nome: {modelo['nome']}")
    print(f"Categoria: {modelo['categoria']}")


def _exibir_marcas():
    """Mostra as marcas para seleção e informa se há opções cadastradas."""
    marcas = listar_marcas()
    if not marcas:
        print(
            'Nenhuma marca cadastrada. Cadastre uma marca antes de cadastrar modelos.'
        )
        return False
    print('\nMarcas cadastradas:')
    for marca in marcas:
        print(f"{marca['id_marca']} - {marca['nome']}")
    return True


def tela_cadastrar_modelo(funcionario):
    """Solicita marca, nome e categoria para cadastrar um modelo."""
    limpar_terminal()
    print('\n--- Cadastrar modelo ---')
    try:
        exigir_administrador(funcionario)
        if not _exibir_marcas():
            return
        id_marca = input('ID da marca: ')
        nome = input('Nome do modelo: ')
        categoria = input('Categoria (hatch/sedan/suv/picape): ')
        cadastrar_modelo(id_marca, nome, categoria, funcionario)
        print('Modelo cadastrado com sucesso!')
    except (ValueError, PermissionError) as erro:
        print(erro)
    except psycopg.Error:
        print('Não foi possível cadastrar o modelo.')


def tela_listar_modelos(funcionario):
    """Exibe os modelos e as marcas correspondentes."""
    limpar_terminal()
    print('\n--- Modelos cadastrados ---')
    try:
        modelos = listar_modelos(funcionario)
        if not modelos:
            print('Nenhum modelo cadastrado.')
            return
        for modelo in modelos:
            _exibir_modelo(modelo)
    except (ValueError, PermissionError) as erro:
        print(erro)
    except psycopg.Error:
        print('Não foi possível listar os modelos.')


def tela_buscar_modelo(funcionario):
    """Solicita um ID e apresenta o modelo encontrado."""
    limpar_terminal()
    print('\n--- Buscar modelo por ID ---')
    try:
        id_modelo = input('ID do modelo: ')
        _exibir_modelo(buscar_modelo(id_modelo, funcionario))
    except (ValueError, PermissionError) as erro:
        print(erro)
    except psycopg.Error:
        print('Não foi possível buscar o modelo.')


def tela_atualizar_modelo(funcionario):
    """Permite alterar campos escolhidos ou todos os dados do modelo."""
    limpar_terminal()
    print('\n--- Atualizar modelo ---')
    try:
        id_modelo = input('ID do modelo: ')
        modelo = buscar_modelo(id_modelo, funcionario)
        _exibir_modelo(modelo)

        print('\nO que deseja atualizar?')
        print('1 - Marca')
        print('2 - Nome')
        print('3 - Categoria')
        print('4 - Todos os dados')
        print('0 - Voltar')
        opcao = input('Opção: ').strip()
        if opcao == '0':
            return
        if opcao not in ('1', '2', '3', '4'):
            print('Opção inválida.')
            return

        id_marca = modelo['id_marca']
        nome = modelo['nome']
        categoria = modelo['categoria']
        print('\nPressione Enter para manter o valor atual.')
        if opcao in ('1', '4'):
            if not _exibir_marcas():
                return
            id_marca = input('ID da marca: ').strip() or id_marca
        if opcao in ('2', '4'):
            nome = input('Nome do modelo: ').strip() or nome
        if opcao in ('3', '4'):
            categoria = (
                input('Categoria (hatch/sedan/suv/picape): ').strip() or categoria
            )

        atualizar_modelo(id_modelo, id_marca, nome, categoria, funcionario)
        print('Modelo atualizado com sucesso!')
    except (ValueError, PermissionError) as erro:
        print(erro)
    except psycopg.Error:
        print('Não foi possível atualizar o modelo.')


def tela_excluir_modelo(funcionario):
    """Apresenta o modelo e solicita confirmação da exclusão."""
    limpar_terminal()
    print('\n--- Excluir modelo ---')
    try:
        id_modelo = input('ID do modelo: ')
        modelo = buscar_modelo(id_modelo, funcionario)
        _exibir_modelo(modelo)
        confirmacao = input('\nDeseja excluir este modelo? (s/n): ').strip().lower()
        if confirmacao != 's':
            print('Exclusão cancelada.')
            return
        excluir_modelo(id_modelo, funcionario)
        print('Modelo excluído com sucesso!')
    except (ValueError, PermissionError) as erro:
        print(erro)
    except psycopg.Error:
        print('Não foi possível excluir o modelo.')


def menu_modelos(funcionario):
    """Restringe o acesso ao administrador e exibe as opções de modelos."""
    try:
        exigir_administrador(funcionario)
    except PermissionError as erro:
        print(erro)
        pausar_terminal()
        return

    while True:
        limpar_terminal()
        print('\n--- Modelos ---')
        print('1 - Cadastrar modelo')
        print('2 - Listar modelos')
        print('3 - Buscar modelo por ID')
        print('4 - Atualizar modelo')
        print('5 - Excluir modelo')
        print('0 - Voltar')
        opcao = input('Opção: ').strip()

        if opcao == '1':
            tela_cadastrar_modelo(funcionario)
        elif opcao == '2':
            tela_listar_modelos(funcionario)
        elif opcao == '3':
            tela_buscar_modelo(funcionario)
        elif opcao == '4':
            tela_atualizar_modelo(funcionario)
        elif opcao == '5':
            tela_excluir_modelo(funcionario)
        elif opcao == '0':
            return
        else:
            print('Opção inválida.')
        pausar_terminal()
