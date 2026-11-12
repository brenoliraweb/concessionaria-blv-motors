from src.utils.terminal import limpar_terminal, pausar_terminal
from src.services.funcionarios_service import cadastrar_funcionario

def menu_funcionarios():
    """
        Exibe as opções de funcionários e informa que as telas estão em desenvolvimento.
    """
    while True:
        limpar_terminal()
        print('\n--- Funcionários ---')
        print('1 - Cadastrar funcionário')
        print('2 - Listar funcionários')
        print('3 - Buscar funcionário')
        print('4 - Atualizar funcionário')
        print('5 - Alterar login e senha')
        print('6 - Excluir funcionário')
        print('7 - Elevar cargo para administrador')
        print('0 - Voltar')

        opcao = input('Opção: ').strip()

        if opcao in ('1', '2', '3', '4', '5', '6', '7'):
            print('Em desenvolvimento.')
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

    pausar_terminal()
