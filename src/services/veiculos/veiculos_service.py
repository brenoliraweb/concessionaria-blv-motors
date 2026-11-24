import psycopg

from src.repositories.veiculos.veiculos_repository import (
    inserir_veiculo,
    listar_veiculos as listar_veiculos_repository,
    buscar_veiculo_por_id,
    atualizar_veiculo as atualizar_veiculo_repository,
    excluir_veiculo as excluir_veiculo_repository
)
from src.utils.validators import (
    validate_id,
    validate_chassis,
    validate_plate,
    validate_text,
    validate_money
)

def validate_year(value):
    try:
        value = int(value)
    except (ValueError, TypeError):
        raise ValueError('Informe um ano válido.')

    if value < 1900:
        raise ValueError('O ano deve ser igual ou superior a 1900.')

    return value

def cadastrar_veiculo(id_modelo, chassi, placa, ano_fabricacao,cor, preco_anunciado):
    id_modelo = validate_id(id_modelo)
    chassi = validate_chassis(chassi)
    placa = validate_plate(placa)
    ano_fabricacao = validate_year(ano_fabricacao)
    cor = validate_text(cor, 30)
    preco_anunciado = validate_money(preco_anunciado)

    try:
        inserir_veiculo(id_modelo, chassi, placa,ano_fabricacao, cor, preco_anunciado)

    except psycopg.errors.UniqueViolation:
        raise ValueError('Chassi ou placa já cadastrado.')

    except psycopg.errors.ForeignKeyViolation:
        raise ValueError('Modelo não encontrado.')

def listar_veiculos():
    return listar_veiculos_repository()

def buscar_veiculo(id_veiculo):
    id_veiculo = validate_id(id_veiculo)
    veiculo = buscar_veiculo_por_id(id_veiculo)

    if veiculo is None:
        raise ValueError('Veículo não encontrado.')

    return veiculo

def atualizar_veiculo(id_veiculo, id_modelo, chassi, placa,ano_fabricacao, cor, preco_anunciado):
    id_veiculo = validate_id(id_veiculo)
    id_modelo = validate_id(id_modelo)
    chassi = validate_chassis(chassi)
    placa = validate_plate(placa)
    ano_fabricacao = validate_year(ano_fabricacao)
    cor = validate_text(cor, 30)
    preco_anunciado = validate_money(preco_anunciado)

    try:
        atualizado = atualizar_veiculo_repository(id_veiculo, id_modelo, chassi, placa,ano_fabricacao, cor, preco_anunciado)

    except psycopg.errors.UniqueViolation:
        raise ValueError('Chassi ou placa já cadastrado.')

    except psycopg.errors.ForeignKeyViolation:
        raise ValueError('Modelo não encontrado.')

    if not atualizado:
        raise ValueError('Veículo não encontrado.')

def excluir_veiculo(id_veiculo):
    id_veiculo = validate_id(id_veiculo)

    try:
        excluido = excluir_veiculo_repository(id_veiculo)

    except psycopg.errors.ForeignKeyViolation:
        raise ValueError(
            'Não é possível excluir: o veículo possui uma venda registrada.'
        )

    if not excluido:
        raise ValueError('Veículo não encontrado.')