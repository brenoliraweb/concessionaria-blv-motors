from src.config.database import connection_database


def inserir_veiculo(id_modelo, chassi, placa, ano_fabricacao, cor, preco_anunciado):
    sql = """
        INSERT INTO veiculos (
            id_modelo, chassi, placa,
            ano_fabricacao, cor, preco_anunciado
        )
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    
    with connection_database() as conn:
        with conn.cursor() as cur:
            cur.execute(
                sql,
                (id_modelo, chassi, placa,ano_fabricacao, cor, preco_anunciado)
            )
        conn.commit()

def listar_veiculos():
    sql = """
        SELECT v.id_veiculo, v.chassi, v.placa,
               v.ano_fabricacao, v.cor, v.preco_anunciado,
               m.nome AS modelo, ma.nome AS marca
        FROM veiculos v
        JOIN modelos m ON m.id_modelo = v.id_modelo
        JOIN marcas ma ON ma.id_marca = m.id_marca
        ORDER BY ma.nome, m.nome, v.id_veiculo
    """

    with connection_database() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()
          
def buscar_veiculo_por_id(id_veiculo):
    """
        Retorna o veículo com sua marca e modelo ou None quando não existe.
    """

    sql = """
        SELECT v.*, m.nome AS modelo, ma.nome AS marca
        FROM veiculos v
        JOIN modelos m ON m.id_modelo = v.id_modelo
        JOIN marcas ma ON ma.id_marca = m.id_marca
        WHERE v.id_veiculo = %s
    """

    with connection_database() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (id_veiculo,))
            return cur.fetchone()

def atualizar_veiculo(id_veiculo, id_modelo, chassi, placa,ano_fabricacao, cor, preco_anunciado):
    """
        Atualiza os dados e informa se algum veículo foi encontrado.
    """

    sql = """
        UPDATE veiculos
        SET id_modelo = %s,
            chassi = %s,
            placa = %s,
            ano_fabricacao = %s,
            cor = %s,
            preco_anunciado = %s
        WHERE id_veiculo = %s
    """

    with connection_database() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (id_modelo, chassi, placa, ano_fabricacao,cor, preco_anunciado, id_veiculo))
            return cur.rowcount > 0

def excluir_veiculo(id_veiculo):
    """
        Exclui o veículo e informa se algum registro foi removido.
    """

    sql = """
        DELETE FROM veiculos
        WHERE id_veiculo = %s
    """

    with connection_database() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (id_veiculo,))
            return cur.rowcount > 0