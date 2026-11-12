import psycopg

from src.repositories.clientes_repository import (
    inserir_cliente,
    listar_clientes as listar_clientes_repository
)
from src.utils.validators import (
  validate_text,
  validate_cpf,
  validate_phone,
  validate_email
)

def cadastrar_cliente(nome, cpf, telefone, email=None):
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
    return listar_clientes_repository()