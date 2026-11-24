import psycopg

from src.services.modelos.modelos_service import listar_modelos
from src.services.veiculos.veiculos_service import (
    atualizar_veiculo,
    buscar_veiculo,
    cadastrar_veiculo,
    excluir_veiculo,
    listar_veiculos,
)
from src.utils.terminal import limpar_terminal, pausar_terminal


def tela_cadastrar_veiculo():
    limpar_terminal()
    print('\n--- Cadastrar veículo ---')

    try:
        modelos = listar_modelos()

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
            preco_anunciado
        )

        print('Veículo cadastrado com sucesso!')

    except ValueError as erro:
        print(erro)

    except psycopg.Error:
        print('Não foi possível cadastrar o veículo.')

def tela_listar_veiculos():
    limpar_terminal()
    print('\n--- Veículos cadastrados ---')

    try:
        veiculos = listar_veiculos()

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

    except psycopg.Error:
        print('Não foi possível listar os veículos.')

def tela_atualizar_veiculo():
    """Permite alterar campos escolhidos ou todos os dados do veículo."""
    limpar_terminal()
    print('\n--- Atualizar veículo ---')

    try:
        id_veiculo = input('ID do veículo: ')
        veiculo = buscar_veiculo(id_veiculo)

        print(f"\nID: {veiculo['id_veiculo']}")
        print(f"Marca: {veiculo['marca']}")
        print(f"Modelo: {veiculo['modelo']}")
        print(f"Chassi: {veiculo['chassi']}")
        print(f"Placa: {veiculo['placa'] or 'Não informada'}")
        print(f"Ano de fabricação: {veiculo['ano_fabricacao']}")
        print(f"Cor: {veiculo['cor']}")
        print(f"Preço anunciado: R$ {veiculo['preco_anunciado']:.2f}")

        print('\nO que deseja atualizar?')
        print('1 - Modelo')
        print('2 - Chassi')
        print('3 - Placa')
        print('4 - Ano de fabricação')
        print('5 - Cor')
        print('6 - Preço anunciado')
        print('7 - Todos os dados')
        print('0 - Voltar')

        opcao = input('Opção: ').strip()

        if opcao == '0':
            return

        if opcao not in ('1', '2', '3', '4', '5', '6', '7'):
            print('Opção inválida.')
            return

        id_modelo = veiculo['id_modelo']
        chassi = veiculo['chassi']
        placa = veiculo['placa'] or ''
        ano_fabricacao = veiculo['ano_fabricacao']
        cor = veiculo['cor']
        preco_anunciado = str(veiculo['preco_anunciado'])

        print('\nPressione Enter para manter o valor atual.')

        if opcao in ('1', '7'):
            print('\n--- Modelos cadastrados ---')

            for modelo in listar_modelos():
                print(
                    f"{modelo['id_modelo']} - "
                    f"{modelo['marca']} {modelo['nome']}"
                )

            id_modelo = input('ID do modelo: ').strip() or id_modelo

        if opcao in ('2', '7'):
            chassi = input('Chassi: ').strip() or chassi

        if opcao in ('3', '7'):
            nova_placa = input('Placa (- para remover): ').strip()

            if nova_placa == '-':
                placa = ''
            elif nova_placa:
                placa = nova_placa

        if opcao in ('4', '7'):
            ano_fabricacao = (
                input('Ano de fabricação: ').strip() or ano_fabricacao
            )

        if opcao in ('5', '7'):
            cor = input('Cor: ').strip() or cor

        if opcao in ('6', '7'):
            preco_anunciado = (
                input('Preço anunciado: ').strip() or preco_anunciado
            )

        atualizar_veiculo(
            id_veiculo,
            id_modelo,
            chassi,
            placa,
            ano_fabricacao,
            cor,
            preco_anunciado,
        )
        print('Veículo atualizado com sucesso!')

    except ValueError as erro:
        print(erro)

    except psycopg.Error:
        print('Não foi possível atualizar o veículo.')

def tela_buscar_veiculo():
    limpar_terminal()
    print('\n--- Buscar veículo por ID ---')

    try:
        id_veiculo = input('ID do veículo: ').strip()
        veiculo = buscar_veiculo(id_veiculo)

        print(f"\nID: {veiculo['id_veiculo']}")
        print(f"Marca: {veiculo['marca']}")
        print(f"Modelo: {veiculo['modelo']}")
        print(f"Chassi: {veiculo['chassi']}")
        print(f"Placa: {veiculo['placa'] or 'Não informada'}")
        print(f"Ano de fabricação: {veiculo['ano_fabricacao']}")
        print(f"Cor: {veiculo['cor']}")
        print(f"Preço anunciado: R$ {veiculo['preco_anunciado']:.2f}")

    except ValueError as erro:
        print(erro)

    except psycopg.Error:
        print('Não foi possível buscar o veículo.')

def tela_excluir_veiculo():
    limpar_terminal()
    print('\n--- Excluir veículo ---')

    try:
        id_veiculo = input('ID do veículo: ').strip()
        veiculo = buscar_veiculo(id_veiculo)

        print(f"\nVeículo: {veiculo['marca']} {veiculo['modelo']}")
        print(f"Chassi: {veiculo['chassi']}")
        print(f"Placa: {veiculo['placa'] or 'Não informada'}")

        confirmacao = input('\nDeseja excluir este veículo? (s/n): ').strip().lower()
        if confirmacao != 's':
            print('Exclusão cancelada.')
            return

        excluir_veiculo(id_veiculo)
        print('Veículo excluído com sucesso!')

    except ValueError as erro:
        print(erro)

    except psycopg.Error:
        print('Não foi possível excluir o veículo.')

def menu_veiculos():
    while True:
        limpar_terminal()
        print('\n--- Veículos ---')
        print('1 - Cadastrar veículo')
        print('2 - Listar todos os veículos')
        print('3 - Buscar veículo por ID')
        print('4 - Atualizar veículo')
        print('5 - Excluir veículo')
        print('0 - Voltar')

        opcao = input('Opção: ').strip()

        if opcao == '1':
            tela_cadastrar_veiculo()

        elif opcao == '2':
            tela_listar_veiculos()

        elif opcao == '3':
            tela_buscar_veiculo()

        elif opcao == '4':
            tela_atualizar_veiculo()

        elif opcao == '5':
            tela_excluir_veiculo()

        elif opcao == '0':
            return

        else:
            print('Opção inválida.')

        pausar_terminal()