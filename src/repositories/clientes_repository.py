"""Comandos SQL para cadastrar, consultar, atualizar e excluir clientes."""

from src.config.database import connection_database


def inserir_cliente(nome, cpf, telefone, email):
    """Insere um cliente e confirma a transação ao sair da conexão."""
    sql = """
        INSERT INTO clientes (nome, cpf, telefone, email)
        VALUES (%s, %s, %s, %s)
    """

    with connection_database() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (nome, cpf, telefone, email))


def listar_clientes():
    """Retorna os clientes em ordem alfabética pelo nome."""
    sql = """
        SELECT id_cliente, nome, cpf, telefone, email
        FROM clientes
        ORDER BY nome
    """

    with connection_database() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()


def listar_clientes_por_id(id_cliente):
    """Retorna o cliente do ID informado ou None quando não existe."""
    sql = """
        SELECT id_cliente, nome, cpf, telefone, email
        FROM clientes
        WHERE id_cliente = %s
    """

    with connection_database() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id_cliente,))
            return cursor.fetchone()


def buscar_cliente_por_cpf(cpf):
    """Retorna o cliente do CPF informado ou None quando não existe."""
    sql = """
        SELECT id_cliente, nome, cpf, telefone, email
        FROM clientes
        WHERE cpf = %s
    """

    with connection_database() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (cpf,))
            return cursor.fetchone()


def atualizar_cliente(id_cliente, nome, cpf, telefone, email):
    """Atualiza os dados e informa se algum cliente foi encontrado."""
    sql = """
        UPDATE clientes
        SET nome = %s,
            cpf = %s,
            telefone = %s,
            email = %s
        WHERE id_cliente = %s
    """

    with connection_database() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (nome, cpf, telefone, email, id_cliente))
            return cursor.rowcount > 0


def excluir_cliente(id_cliente):
    """Exclui o cliente e informa se algum registro foi removido."""
    sql = """
        DELETE FROM clientes
        WHERE id_cliente = %s
    """

    with connection_database() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id_cliente,))
            return cursor.rowcount > 0
