"""Regras de acesso, validação e gerenciamento de modelos."""

import psycopg

from src.repositories import modelos_repository as rep
from src.utils.validators import validate_id, validate_text


def exigir_administrador(funcionario):
    """O gerenciamento de modelos é exclusivo do administrador (RN12)."""
    if not funcionario or funcionario.get('cargo') != 'admin':
        raise PermissionError('Somente administradores podem gerenciar modelos.')


def _validar_dados(id_marca, nome, categoria):
    """Valida a marca, o nome e uma das quatro categorias permitidas."""
    id_marca = validate_id(id_marca)
    nome = validate_text(nome, 100)
    categoria = validate_text(categoria, 20).lower()

    if categoria not in ('hatch', 'sedan', 'suv', 'picape'):
        raise ValueError('A categoria deve ser hatch, sedan, suv ou picape.')

    return id_marca, nome, categoria


def cadastrar_modelo(id_marca, nome, categoria, funcionario=None):
    """Exige administrador e trata marca inexistente ou modelo repetido."""
    exigir_administrador(funcionario)
    dados = _validar_dados(id_marca, nome, categoria)
    try:
        return rep.inserir_modelo(*dados)
    except psycopg.errors.UniqueViolation:
        raise ValueError('Já existe um modelo com esse nome nesta marca.') from None
    except psycopg.errors.ForeignKeyViolation:
        raise ValueError('Marca não encontrada.') from None


def listar_modelos(funcionario=None):
    """Retorna os modelos cadastrados para consulta administrativa."""
    exigir_administrador(funcionario)
    return rep.listar_modelos()


def buscar_modelo(id_modelo, funcionario=None):
    """Valida o ID e informa quando o modelo não existe."""
    exigir_administrador(funcionario)
    modelo = rep.buscar_modelo(validate_id(id_modelo))
    if not modelo:
        raise ValueError('Modelo não encontrado.')
    return modelo


def atualizar_modelo(id_modelo, id_marca, nome, categoria, funcionario=None):
    """Valida os novos dados e trata conflitos de marca e nome."""
    exigir_administrador(funcionario)
    id_modelo = validate_id(id_modelo)
    dados = _validar_dados(id_marca, nome, categoria)
    try:
        atualizado = rep.atualizar_modelo(id_modelo, *dados)
    except psycopg.errors.UniqueViolation:
        raise ValueError('Já existe um modelo com esse nome nesta marca.') from None
    except psycopg.errors.ForeignKeyViolation:
        raise ValueError('Marca não encontrada.') from None
    if not atualizado:
        raise ValueError('Modelo não encontrado.')


def excluir_modelo(id_modelo, funcionario=None):
    """Exige administrador e impede excluir modelo com veículos vinculados."""
    exigir_administrador(funcionario)
    try:
        excluido = rep.excluir_modelo(validate_id(id_modelo))
    except psycopg.errors.ForeignKeyViolation:
        raise ValueError(
            'Não é possível excluir: existem veículos vinculados ao modelo.'
        ) from None
    if not excluido:
        raise ValueError('Modelo não encontrado.')
