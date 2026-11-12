from config.database import connection_database


def criar_funcionario(nome, cpf, telefone, cargo, login, senha_hash):
    sql = """
        INSERT INTO funcionarios (nome, cpf, telefone, cargo, login, senha_hash)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id_funcionario;
    """

    with connection_database() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (nome, cpf, telefone, cargo, login, senha_hash))
            return cur.fetchone()[0]


def listar_funcionarios():
    sql = """
        SELECT id_funcionario, nome, cpf, telefone, cargo
        FROM funcionarios
        ORDER BY nome;
    """

    with connection_database() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()


def listar_funcionario_por_id(id_funcionario):
    sql = """
        SELECT id_funcionario, nome, cpf, telefone, cargo, login
        FROM funcionarios
        WHERE id_funcionario = %s;
    """

    with connection_database() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (id_funcionario,))
            return cur.fetchone()

def listar_funcionario_por_login(login):
    sql = """
        SELECT id_funcionario, nome, cpf, telefone, cargo
        FROM funcionarios
        WHERE login = %s;
    """
    with connection_database() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (login,))
            return cur.fetchone()

def atualizar_funcionario(nome, cpf, telefone, cargo, id_funcionario):
    sql = """
        UPDATE funcionarios
        SET nome = %s,
            cpf = %s,
            telefone = %s,
            cargo = %s
        WHERE id_funcionario = %s;
    """

    with connection_database() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (nome, cpf, telefone, cargo, id_funcionario))
            return cur.rowcount > 0


def atualizar_login_funcionario(login, senha_hash, id_funcionario):
    sql = """
        UPDATE funcionarios
        SET login = %s,
            senha_hash = %s
        WHERE id_funcionario = %s;
    """

    with connection_database() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (login, senha_hash, id_funcionario))
            return cur.rowcount > 0


def deletar_funcionario(id_funcionario):
    sql = """
        DELETE FROM funcionarios
        WHERE id_funcionario = %s;
    """

    with connection_database() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (id_funcionario,))
            return cur.rowcount > 0