from src.config.database import connection_database

def inserir_cliente(nome, cpf, telefone, email):
  with connection_database() as con:
      with con.cursor() as cursor:
        cursor.execute(
          """
          INSERT INTO clientes(nome, cpf, telefone, email)
          VALUES(%s, %s, %s, %s)
          RETURNING id_cliente, nome
          """,
          (nome, cpf, telefone, email)
        )
      con.commit()
        
