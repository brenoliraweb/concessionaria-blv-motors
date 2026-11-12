from src.config.database import test_connection
from src.views import clientes_views


def menu_clientes():
    while True:
        print('\n--- Clientes ---')
        print('1 - Cadastrar cliente')
        print('2 - Listar clientes')
        print('3 - Buscar cliente')
        print('4 - Atualizar cliente')
        print('5 - Excluir cliente')
        print('0 - Voltar')

        opcao = input('Opção: ').strip()

        if opcao == '1':
            clientes_views.tela_cadastrar_cliente()

        elif opcao == '2':
            clientes_views.tela_listar_clientes()

        elif opcao in ('3', '4', '5'):
            # Substituir pelas chamadas quando estiverem prontas.
            print('Em desenvolvimento.')

        elif opcao == '0':
            break

        else:
            print('Opção inválida.')


def menu_funcionarios():
    while True:
        print('\n--- Funcionários ---')
        print('1 - Cadastrar funcionário')
        print('2 - Listar funcionários')
        print('3 - Buscar funcionário')
        print('4 - Atualizar funcionário')
        print('5 - Alterar login e senha')
        print('6 - Excluir funcionário')
        print('0 - Voltar')

        opcao = input('Opção: ').strip()

        if opcao in ('1', '2', '3', '4', '5', '6'):
            # Conectar à view de funcionários quando estiver pronta.
            print('Em desenvolvimento.')

        elif opcao == '0':
            break

        else:
            print('Opção inválida.')


def main():
    while True:
        print('\n--- BLV Motors ---')
        print('1 - Clientes')
        print('2 - Funcionários')
        print('0 - Sair')

        opcao = input('Opção: ').strip()

        if opcao == '1':
            menu_clientes()

        elif opcao == '2':
            menu_funcionarios()

        elif opcao == '0':
            print('Programa encerrado.')
            break

        else:
            print('Opção inválida.')




if __name__ == '__main__':
    try:
        print('Iniciando a aplicação...')
        test_connection()
        main()
    except (KeyboardInterrupt, EOFError):
        print('\nPrograma encerrado.')
  