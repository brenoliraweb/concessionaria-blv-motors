from src.config.database import connection_database


def inserir_cliente(nome, cpf, telefone, email):
    """
        Insere os dados de um cliente no banco de dados.
    """
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
    """
        Consulta e retorna os clientes cadastrados, ordenados pelo nome.
    """
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
              (id_cliente,)
          )
          return cursor.fetchone()
        
def buscar_cliente_por_cpf(cpf):
    with connection_database() as con:
        with con.cursor() as cursor:
            cursor.execute(
                """
                SELECT id_cliente, nome, cpf, telefone, email
                FROM clientes
                WHERE cpf = %s
                """,
                (cpf,)
            )

            return cursor.fetchone()

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
      
def excluir_cliente(id_cliente):
    with connection_database() as con:
      with con.cursor() as cursor:
        cursor.execute(
          """
          DELETE FROM clientes WHERE id_cliente = %s
          """,
          (id_cliente,)
        )
        excluido = cursor.rowcount > 0
      con.commit()
      return excluido