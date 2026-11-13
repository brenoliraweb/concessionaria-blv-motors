"""Validações e tratamento dos erros do cadastro de marcas."""

import psycopg

from src.repositories.marcas_repository import (
    atualizar_marca as atualizar_marca_repository,
    buscar_marca_por_id,
    excluir_marca as excluir_marca_repository,
    inserir_marca,
    listar_marcas as listar_marcas_repository,
)

from src.utils.validators import validate_id, validate_text


def cadastrar_marca(nome):
    """Valida o nome e trata a tentativa de cadastrar uma marca repetida."""
    nome = validate_text(nome, 50)

    try:
        inserir_marca(nome)

    except psycopg.errors.UniqueViolation:
        raise ValueError('Marca já cadastrada.')


def listar_marcas():
    """Consulta as marcas cadastradas pelo repositório."""
    return listar_marcas_repository()


def buscar_marca(id_marca):
    """Valida o ID e informa quando a marca não existe."""
    id_marca = validate_id(id_marca)
    marca = buscar_marca_por_id(id_marca)

    if marca is None:
        raise ValueError('Marca não encontrada.')

    return marca


def atualizar_marca(id_marca, nome):
    """Valida o novo nome e trata marca repetida ou inexistente."""
    id_marca = validate_id(id_marca)
    nome = validate_text(nome, 50)

    try:
        atualizado = atualizar_marca_repository(id_marca, nome)

    except psycopg.errors.UniqueViolation:
        raise ValueError('Marca já cadastrada.')

    if not atualizado:
        raise ValueError('Marca não encontrada.')


def excluir_marca(id_marca):
    """Exclui a marca quando não existem modelos vinculados."""
    id_marca = validate_id(id_marca)

    try:
        excluido = excluir_marca_repository(id_marca)

    except psycopg.errors.ForeignKeyViolation:
        raise ValueError(
            'Não é possível excluir: existem modelos vinculados à marca.'
        )

    if not excluido:
        raise ValueError('Marca não encontrada.')
