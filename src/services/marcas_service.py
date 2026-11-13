import psycopg

from src.repositories.marcas_repository import (
    inserir_marca,
    listar_marcas as listar_marcas_repository,
    buscar_marca_por_id,
    atualizar_marca as atualizar_marca_repository,
    excluir_marca as excluir_marca_repository
)

from src.utils.validators import validate_text, validate_id


def cadastrar_marca(nome):
    nome = validate_text(nome, 50)

    try:
        inserir_marca(nome)

    except psycopg.errors.UniqueViolation:
        raise ValueError('Marca já cadastrada.')

def listar_marcas():
    return listar_marcas_repository()

def buscar_marca(id_marca):
    id_marca = validate_id(id_marca)
    marca = buscar_marca_por_id(id_marca)

    if marca is None:
        raise ValueError('Marca não encontrada.')

    return marca

def atualizar_marca(id_marca, nome):
    id_marca = validate_id(id_marca)
    nome = validate_text(nome, 50)

    try:
        atualizado = atualizar_marca_repository(id_marca, nome)

    except psycopg.errors.UniqueViolation:
        raise ValueError('Marca já cadastrada.')

    if not atualizado:
        raise ValueError('Marca não encontrada.')

def excluir_marca(id_marca):
    id_marca = validate_id(id_marca)

    try:
        excluido = excluir_marca_repository(id_marca)

    except psycopg.errors.ForeignKeyViolation:
        raise ValueError(
            'Não é possível excluir: existem modelos vinculados à marca.'
        )

    if not excluido:
        raise ValueError('Marca não encontrada.')