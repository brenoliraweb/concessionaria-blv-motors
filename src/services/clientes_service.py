import psycopg

from src.repositories.clientes_repository import (
    inserir_cliente,
    listar_clientes as listar_clientes_repository,
    listar_clientes_por_id as listar_clientes_por_id_repository,
    atualizar_cliente as atualizar_cliente_repository,
    excluir_cliente as excluir_cliente_repository
)

from src.utils.validators import (
  validate_text,
  validate_cpf,
  validate_phone,
  validate_email,
  validate_id
)

def cadastrar_cliente(nome, cpf, telefone, email=None):
  """
      Valida os dados do cliente e solicita o cadastro, tratando CPF ou e-mail duplicados.
  """
  nome = validate_text(nome, 250)
  cpf = validate_cpf(cpf)
  telefone = validate_phone(telefone)

  if isinstance(email,str):
    email = email.strip() or None

  email = validate_email(email)

  try:
    inserir_cliente(nome, cpf, telefone, email)
  except psycopg.errors.UniqueViolation:
    raise ValueError("CPF ou email já cadastrado.")

def listar_clientes():
    """
        Retorna os clientes cadastrados consultando o repositório.
    """
    return listar_clientes_repository()

def listar_cliente_por_id(id_cliente):
    id_cliente = validate_id(id_cliente)
    cliente = listar_clientes_por_id_repository(id_cliente)

    if cliente is None:
        raise ValueError('Cliente não encontrado.')

    return cliente

def atualizar_cliente(id_cliente, nome, cpf, telefone, email=None):
    id_cliente = validate_id(id_cliente)
    nome = validate_text(nome, 250)
    cpf = validate_cpf(cpf)
    telefone = validate_phone(telefone)

    if isinstance(email, str):
        email = email.strip() or None

    email = validate_email(email)

    try:
        atualizado = atualizar_cliente_repository(
            id_cliente, nome, cpf, telefone, email
        )
    except psycopg.errors.UniqueViolation:
        raise ValueError('CPF ou e-mail já cadastrado.') from None

    if not atualizado:
        raise ValueError('Cliente não encontrado.')
      
def excluir_cliente(id_cliente, funcionario):
    if not funcionario or funcionario.get('cargo') != 'admin':
        raise PermissionError('Você não tem permissão para excluir clientes.')

    id_cliente = validate_id(id_cliente)

    try:
        excluido = excluir_cliente_repository(id_cliente)

    except psycopg.errors.ForeignKeyViolation:
        raise ValueError('Não é possível excluir: o cliente possui vendas registradas.')

    if not excluido:
        raise ValueError('Cliente não encontrado.')