import psycopg

from src.repositories.vendas.vendas_repository import inserir_venda
from src.utils.validators import validate_id, validate_money

def registrar_venda(id_cliente, id_funcionario, id_veiculo, valor_venda, forma_pagamento):
    id_cliente = validate_id(id_cliente)
    id_funcionario = validate_id(id_funcionario)
    id_veiculo = validate_id(id_veiculo)
    valor_venda = validate_money(valor_venda)
    forma_pagamento = forma_pagamento.strip().lower()

    if forma_pagamento not in ('dinheiro', 'pix', 'cartao', 'financiamento'):
        raise ValueError('Forma de pagamento inválida.')

    try:
        inserir_venda(id_cliente, id_funcionario, id_veiculo, valor_venda, forma_pagamento)

    except psycopg.errors.UniqueViolation:
        raise ValueError('Este veículo já possui uma venda registrada.')

    except psycopg.errors.ForeignKeyViolation:
        raise ValueError('Cliente, funcionário ou veículo não encontrado.')