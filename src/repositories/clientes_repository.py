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

def listar_clientes_por_id(id_cliente):
    with connection_database() as con:
        with con.cursor() as cursor:
          cursor.execute(
              """
              SELECT id_cliente, nome, cpf, telefone, email 
              FROM clientes 
              WHERE id_cliente = %s 
              """,
              (id_cliente)
          )
          return cursor.fetchone

def atualizar_cliente(id_cliente, nome, cpf, telefone, email):
    with connection_database() as con:
        with con.cursor() as cursor:
          cursor.execute(
            """   
            UPDATE clientes
            SET nome = %s, cpf = %s, telefone = %s, email = %s
            WHERE id_cliente = %s
            """,
            (nome, cpf, telefone, email, id_cliente)   
        )
          atualizado = cursor.rowcount > 0
        con.commit()
        return atualizado  