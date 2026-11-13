from src.config.database import connection_database


def inserir_marca(nome):
    with connection_database() as con:
        with con.cursor() as cursor:
            cursor.execute(
                "INSERT INTO marcas (nome) VALUES (%s)",
                (nome,)
            )

        con.commit()


def listar_marcas():
    with connection_database() as con:
        with con.cursor() as cursor:
            cursor.execute(
                "SELECT id_marca, nome FROM marcas ORDER BY nome"
            )
            return cursor.fetchall()


def buscar_marca_por_id(id_marca):
    with connection_database() as con:
        with con.cursor() as cursor:
            cursor.execute(
                "SELECT id_marca, nome FROM marcas WHERE id_marca = %s",
                (id_marca,)
            )
            return cursor.fetchone()


def atualizar_marca(id_marca, nome):
    with connection_database() as con:
        with con.cursor() as cursor:
            cursor.execute(
                "UPDATE marcas SET nome = %s WHERE id_marca = %s",
                (nome, id_marca)
            )
            atualizado = cursor.rowcount > 0
        con.commit()
        return atualizado


def excluir_marca(id_marca):
    with connection_database() as con:
        with con.cursor() as cursor:
            cursor.execute(
                "DELETE FROM marcas WHERE id_marca = %s",
                (id_marca,)
            )
            excluido = cursor.rowcount > 0
        con.commit()
        return excluido