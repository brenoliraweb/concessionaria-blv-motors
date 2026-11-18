import psycopg

from src.services.modelos.modelos_service import listar_modelos
from src.services.veiculos.veiculos_service import (
    cadastrar_veiculo,
    listar_veiculos
)
from src.utils.terminal import limpar_terminal, pausar_terminal


def tela_cadastrar_veiculo(funcionario):
    limpar_terminal()
    print('\n--- Cadastrar veículo ---')

    try:
        modelos = listar_modelos(funcionario)

        if not modelos:
            print('Cadastre um modelo antes de cadastrar veículos.')
            return

        print('\n--- Modelos cadastrados ---')

        for modelo in modelos:
            print(
                f"{modelo['id_modelo']} - "
                f"{modelo['marca']} {modelo['nome']}"
            )

        id_modelo = input('\nID do modelo: ')
        chassi = input('Chassi: ')
        placa = input('Placa (opcional): ')
        ano_fabricacao = input('Ano de fabricação: ')
        cor = input('Cor: ')
        preco_anunciado = input('Preço anunciado (ex.: 75000,50): ')

        cadastrar_veiculo(
            id_modelo,
            chassi,
            placa,
            ano_fabricacao,
            cor,
            preco_anunciado,
            funcionario
        )

        print('Veículo cadastrado com sucesso!')

    except (ValueError, PermissionError) as erro:
        print(erro)

    except psycopg.Error:
        print('Não foi possível cadastrar o veículo.')

def tela_listar_veiculos(funcionario):
    limpar_terminal()
    print('\n--- Veículos cadastrados ---')

    try:
        veiculos = listar_veiculos(funcionario)

        if not veiculos:
            print('Nenhum veículo cadastrado.')
            return

        for veiculo in veiculos:
            print(f"\nID: {veiculo['id_veiculo']}")
            print(f"Marca: {veiculo['marca']}")
            print(f"Modelo: {veiculo['modelo']}")
            print(f"Chassi: {veiculo['chassi']}")
            print(f"Placa: {veiculo['placa'] or 'Não informada'}")
            print(f"Ano de fabricação: {veiculo['ano_fabricacao']}")
            print(f"Cor: {veiculo['cor']}")
            print(f"Preço anunciado: R$ {veiculo['preco_anunciado']:.2f}")

    except PermissionError as erro:
        print(erro)

    except psycopg.Error:
        print('Não foi possível listar os veículos.')


def menu_veiculos(funcionario):
    while True:
        limpar_terminal()
        print('\n--- Veículos ---')
        print('1 - Cadastrar veículo')
        print('2 - Listar todos os veículos')
        print('0 - Voltar')

        opcao = input('Opção: ').strip()

        if opcao == '1':
            tela_cadastrar_veiculo(funcionario)

        elif opcao == '2':
            tela_listar_veiculos(funcionario)

        elif opcao == '0':
            return

        else:
            print('Opção inválida.')

        pausar_terminal()