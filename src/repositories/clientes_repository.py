from src.config.database import connection_database


def inserir_cliente(nome, cpf, telefone, email):
    with connection_database() as con:
        with con.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO clientes (nome, cpf, telefone, email)
                VALUES (%s, %s, %s, %s)
                """,
                (nome, cpf, telefone, email)
            )

        con.commit()

def listar_clientes():
    with connection_database() as con:
        with con.cursor() as cursor:
            cursor.execute(
                """
                SELECT id_cliente, nome, cpf, telefone, email
                FROM clientes
                ORDER BY nome
                """
            )
            return cursor.fetchall()        