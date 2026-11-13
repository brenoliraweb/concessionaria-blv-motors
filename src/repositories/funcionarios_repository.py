"""Comandos SQL de funcionários e consulta de credenciais para autenticação."""

from src.config.database import connection_database


def criar_funcionario(nome, cpf, telefone, cargo, login, senha_hash):
    """Insere um funcionário no banco de dados e retorna o ID gerado."""
    sql = """
        INSERT INTO funcionarios (nome, cpf, telefone, cargo, login, senha_hash)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id_funcionario;
    """

    with connection_database() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (nome, cpf, telefone, cargo, login, senha_hash))
            return cursor.fetchone()['id_funcionario']


def listar_funcionarios():
    """Consulta e retorna os funcionários cadastrados, ordenados pelo nome."""
    sql = """
        SELECT id_funcionario, nome, cpf, telefone, cargo
        FROM funcionarios
        ORDER BY nome;
    """

    with connection_database() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()


def listar_funcionario_por_id(id_funcionario):
    """Busca e retorna os dados de um funcionário pelo seu ID."""
    sql = """
        SELECT id_funcionario, nome, cpf, telefone, cargo, login
        FROM funcionarios
        WHERE id_funcionario = %s;
    """

    with connection_database() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id_funcionario,))
            return cursor.fetchone()


def listar_funcionario_por_login(login):
    """
    Busca um funcionário pelo login, incluindo o hash da senha para
    autenticação.
    """
    sql = """
        SELECT id_funcionario, nome, cpf, telefone, cargo, login, senha_hash
        FROM funcionarios
        WHERE login = %s;
    """
    with connection_database() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (login,))
            return cursor.fetchone()


def atualizar_funcionario(nome, cpf, telefone, cargo, id_funcionario):
    """
    Atualiza os dados e o cargo do funcionário e informa se algum registro foi
    alterado.
    """
    sql = """
        UPDATE funcionarios
        SET nome = %s,
            cpf = %s,
            telefone = %s,
            cargo = %s
        WHERE id_funcionario = %s;
    """

    with connection_database() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (nome, cpf, telefone, cargo, id_funcionario))
            return cursor.rowcount > 0


def atualizar_login_funcionario(login, senha_hash, id_funcionario):
    """
    Atualiza o login e o hash da senha e informa se algum registro foi
    alterado.
    """
    sql = """
        UPDATE funcionarios
        SET login = %s,
            senha_hash = %s
        WHERE id_funcionario = %s;
    """

    with connection_database() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (login, senha_hash, id_funcionario))
            return cursor.rowcount > 0


def deletar_funcionario(id_funcionario):
    """Exclui o funcionário pelo ID e informa se algum registro foi removido."""
    sql = """
        DELETE FROM funcionarios
        WHERE id_funcionario = %s;
    """

    with connection_database() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id_funcionario,))
            return cursor.rowcount > 0
