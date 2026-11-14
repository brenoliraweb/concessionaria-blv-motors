from src.config.database import connection_database

def inserir_marca(nome):
    """
        Insere uma marca no banco de dados.
    """

    sql = """
        INSERT INTO marcas (nome)
        VALUES (%s)
    """

    with connection_database() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (nome,))

def listar_marcas():
    """
        Retorna as marcas em ordem alfabética.
    """

    sql = """
        SELECT id_marca, nome
        FROM marcas
        ORDER BY nome
    """

    with connection_database() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()

def buscar_marca_por_id(id_marca):
    """
        Retorna a marca do ID informado ou None quando não existe.
    """

    sql = """
        SELECT id_marca, nome
        FROM marcas
        WHERE id_marca = %s
    """

    with connection_database() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (id_marca,))
            return cur.fetchone()

def atualizar_marca(id_marca, nome):
    """
        Altera o nome da marca e informa se ela foi encontrada.
    """

    sql = """
        UPDATE marcas
        SET nome = %s
        WHERE id_marca = %s
    """

    with connection_database() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (nome, id_marca))
            return cur.rowcount > 0

def excluir_marca(id_marca):
    """
        Exclui a marca e informa se algum registro foi removido.
    """

    sql = """
        DELETE FROM marcas
        WHERE id_marca = %s
    """

    with connection_database() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (id_marca,))
            return cur.rowcount > 0
