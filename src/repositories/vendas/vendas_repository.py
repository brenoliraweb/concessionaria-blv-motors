from src.config.database import connection_database


def inserir_venda(
    id_cliente, id_funcionario, id_veiculo, valor_venda, forma_pagamento
):
    """Registra uma venda no banco de dados."""
    sql = """
        INSERT INTO vendas (id_cliente, id_funcionario, id_veiculo, valor_venda, forma_pagamento)
        VALUES (%s, %s, %s, %s, %s)
    """

    with connection_database() as conn:
        with conn.cursor() as cur:
            cur.execute(sql,(id_cliente,id_funcionario,id_veiculo,valor_venda,forma_pagamento))