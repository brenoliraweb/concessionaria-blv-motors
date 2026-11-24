import psycopg

from src.repositories.modelos import modelos_repository as rep
from src.utils.validators import validate_id, validate_text

def _validar_dados(id_marca, nome, categoria):
    """
        Valida a marca, o nome e uma das quatro categorias permitidas.
    """

    id_marca = validate_id(id_marca)
    nome = validate_text(nome, 100)
    categoria = validate_text(categoria, 20).lower()

    if categoria not in ('hatch', 'sedan', 'suv', 'picape'):
        raise ValueError('A categoria deve ser hatch, sedan, suv ou picape.')

    return id_marca, nome, categoria

def cadastrar_modelo(id_marca, nome, categoria):
    """
        Trata marca inexistente ou modelo repetido.
    """

    dados = _validar_dados(id_marca, nome, categoria)

    try:
        return rep.inserir_modelo(*dados)
    
    except psycopg.errors.UniqueViolation:
        raise ValueError('Já existe um modelo com esse nome nesta marca.') from None
    
    except psycopg.errors.ForeignKeyViolation:
        raise ValueError('Marca não encontrada.') from None

def listar_modelos():
    """
        Retorna os modelos cadastrados para consulta administrativa.
    """

    return rep.listar_modelos()

def buscar_modelo(id_modelo):
    """
        Valida o ID e informa quando o modelo não existe.
    """

    modelo = rep.buscar_modelo(validate_id(id_modelo))

    if not modelo:
        raise ValueError('Modelo não encontrado.')
    
    return modelo

def atualizar_modelo(id_modelo, id_marca, nome, categoria):
    """
        Valida os novos dados e trata conflitos de marca e nome.
    """

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

def excluir_modelo(id_modelo):
    """
        Impede excluir modelo com veículos vinculados.
    """


    try:
        excluido = rep.excluir_modelo(validate_id(id_modelo))

    except psycopg.errors.ForeignKeyViolation:
        raise ValueError('Não é possível excluir: existem veículos vinculados ao modelo.') from None
    
    if not excluido:
        raise ValueError('Modelo não encontrado.')