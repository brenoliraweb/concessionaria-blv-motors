import psycopg

from src.utils.validators import validate_cpf, validate_phone, validate_id
from src.utils.auth.password import  hash_password, verify_password
from src.repositories import funcionarios_repository as rep

def cadastrar_funcionario(nome, cpf, telefone, cargo, login, senha):
    """
        Valida os dados, gera o hash da senha e cadastra o funcionário, tratando CPF ou login duplicados.
    """
    nome = nome.strip()

    if not nome or len(nome) > 250:
        raise ValueError('O nome deve ter entre 1 e 250 caracteres.')

    cpf = validate_cpf(cpf)
    telefone = validate_phone(telefone)

    cargo = cargo.strip().lower()

    if cargo not in ('admin', 'vendedor'):
        raise ValueError('O cargo deve ser admin ou vendedor')

    login = login.strip()

    if not login or len(login) > 50:
        raise ValueError('O login deve ter entre 1 e 50 caracteres.')

    if not senha:
        raise ValueError('A senha é obrigatória.')

    senha_hash = hash_password(senha)

    try:
        return rep.criar_funcionario(nome, cpf, telefone, cargo, login, senha_hash)
    except psycopg.errors.UniqueViolation as erro:
        raise ValueError('CPF ou login já cadastrado.') from erro

def listar_funcionarios():
    """
        Retorna os funcionários cadastrados consultando o repositório.
    """
    return rep.listar_funcionarios()

def listar_funcionario_por_id(id_funcionario):
    """
        Busca o funcionário pelo ID e informa quando o cadastro não existe.
    """
    id_funcionario = validate_id(id_funcionario)
    funcionario = rep.listar_funcionario_por_id(id_funcionario)

    if funcionario is None:
        raise ValueError('Funcionário não encontrado ou não existe.')

    return funcionario

def atualizar_funcionario(nome, cpf, telefone, cargo, id_funcionario):
    """
        Valida e atualiza os dados e o cargo do funcionário, tratando CPF duplicado ou cadastro inexistente.
    """
    id_funcionario = validate_id(id_funcionario)
    nome = nome.strip()
    
    if not nome or len(nome) > 250:
        raise ValueError('O nome deve ter entre 1 e 250 caracteres.')
    
    cpf = validate_cpf(cpf)
    telefone = validate_phone(telefone)
    
    cargo = cargo.strip().lower()
    
    if cargo not in ('admin', 'vendedor'):
        raise ValueError('O cargo deve ser admin ou vendedor')

    try:
        atualizado = rep.atualizar_funcionario(nome, cpf, telefone, cargo, id_funcionario)
    except psycopg.errors.UniqueViolation as erro:
        raise ValueError('CPF já cadastrado.') from erro

    if not atualizado:
        raise ValueError('Funcionário não encontrado ou não existe.')

    return atualizado

def atualizar_login_funcionario(login, senha, id_funcionario):
    """
        Valida e atualiza o login e a senha, tratando login duplicado ou cadastro inexistente.
    """
    id_funcionario = validate_id(id_funcionario)
    login = login.strip()

    if not login or len(login) > 50:
        raise ValueError('O login deve ter entre 1 e 50 caracteres.')

    if not senha:
        raise ValueError('A senha é obrigatória.')

    senha_hash = hash_password(senha)

    try:
        atualizado = rep.atualizar_login_funcionario(login, senha_hash, id_funcionario)
    except psycopg.errors.UniqueViolation as erro:
        raise ValueError('Login já cadastrado.') from erro

    if not atualizado:
        raise ValueError("Funcionário não encontrado.")

    return atualizado

def deletar_funcionario(id_funcionario):
    """
        Solicita a exclusão do funcionário e informa quando o cadastro não existe.
    """
    id_funcionario = validate_id(id_funcionario)

    try:
        deletado = rep.deletar_funcionario(id_funcionario)
    except psycopg.errors.ForeignKeyViolation as erro:
        raise ValueError('Não é possível excluir: o funcionário possui registros vinculados.') from erro

    if not deletado:
        raise ValueError('Funcionário não encontrado ou não existe.')

    return deletado

def autenticar_funcionario(login, senha):
    """
        Valida o login e a senha e retorna o ID, o nome e o cargo do funcionário autenticado.
    """
    login = login.strip()

    funcionario = rep.listar_funcionario_por_login(login)

    if funcionario is None:
        raise ValueError('Login ou senha inválidos.')

    if not verify_password(senha, funcionario["senha_hash"]):
        raise ValueError('Login ou senha inválidos.')

    return {
        'id_funcionario': funcionario['id_funcionario'],
        'nome': funcionario['nome'],
        'cargo': funcionario['cargo']
    }
