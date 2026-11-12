from utils.validators import validate_cpf, validate_phone
from utils.auth.password import  hash_password
from repositories import funcionarios_repository as rep

def cadastrar_funcionario(nome, cpf, telefone, cargo, login, senha):
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

    return rep.criar_funcionario(nome, cpf, telefone, cargo, login, senha_hash)

def listar_funcionarios():
    return rep.listar_funcionarios()

def listar_funcionario_por_id(id_funcionario):
    funcionario = rep.listar_funcionario_por_id(id_funcionario)

    if funcionario is None:
        raise ValueError('Funcionário não encontrado ou não existe.')

    return funcionario

def atualizar_funcionario(nome, cpf, telefone, cargo, id_funcionario):
    nome = nome.strip()
    
    if not nome or len(nome) > 250:
        raise ValueError('O nome deve ter entre 1 e 250 caracteres.')
    
    cpf = validate_cpf(cpf)
    telefone = validate_phone(telefone)
    
    cargo = cargo.strip().lower()
    
    if cargo not in ('admin', 'vendedor'):
        raise ValueError('O cargo deve ser admin ou vendedor')

    atualizado = rep.atualizar_funcionario(nome, cpf, telefone, cargo, id_funcionario)

    if not atualizado:
        raise ValueError('Funcionário não encontrado ou não existe.')

    return atualizado

def atualizar_login_funcionario(login, senha, id_funcionario):
    login = login.strip()

    if not login or len(login) > 50:
        raise ValueError('O login deve ter entre 1 e 50 caracteres.')

    if not senha:
        raise ValueError('A senha é obrigatória.')

    senha_hash = hash_password(senha)

    atualizado = rep.atualizar_login_funcionario(login, senha_hash, id_funcionario)

    if not atualizado:
        raise ValueError("Funcionário não encontrado.")

    return atualizado

def deletar_funcionario(id_funcionario):
    deletado = rep.deletar_funcionario(id_funcionario)

    if not deletado:
        raise ValueError('Funcionário não encontrado ou não existe.')

    return deletado