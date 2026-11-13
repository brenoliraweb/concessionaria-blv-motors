"""Comandos SQL de modelos e consultas das marcas correspondentes."""

from src.config.database import connection_database


def inserir_modelo(id_marca, nome, categoria):
    """Insere um modelo e retorna o ID gerado pelo banco."""
    sql = """
        INSERT INTO modelos (id_marca, nome, categoria)
        VALUES (%s, %s, %s)
        RETURNING id_modelo
    """

    with connection_database() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id_marca, nome, categoria))
            return cursor.fetchone()['id_modelo']


def listar_modelos():
    """Retorna os modelos e suas marcas, ordenados por marca e modelo."""
    sql = """
        SELECT modelos.*, marcas.nome AS marca
        FROM modelos
        JOIN marcas ON marcas.id_marca = modelos.id_marca
        ORDER BY marcas.nome, modelos.nome
    """

    with connection_database() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()


def buscar_modelo(id_modelo):
    """Retorna o modelo e sua marca ou None quando o ID não existe."""
    sql = """
        SELECT modelos.*, marcas.nome AS marca
        FROM modelos
        JOIN marcas ON marcas.id_marca = modelos.id_marca
        WHERE modelos.id_modelo = %s
    """

    with connection_database() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id_modelo,))
            return cursor.fetchone()


def atualizar_modelo(id_modelo, id_marca, nome, categoria):
    """Atualiza marca, nome e categoria e informa se o modelo existe."""
    sql = """
        UPDATE modelos
        SET id_marca = %s,
            nome = %s,
            categoria = %s
        WHERE id_modelo = %s
    """

    with connection_database() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id_marca, nome, categoria, id_modelo))
            return cursor.rowcount > 0


def excluir_modelo(id_modelo):
    """Exclui o modelo e informa se algum registro foi removido."""
    sql = """
        DELETE FROM modelos
        WHERE id_modelo = %s
    """

    with connection_database() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id_modelo,))
            return cursor.rowcount > 0
