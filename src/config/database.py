import os
import psycopg

from psycopg.rows import dict_row
from dotenv import load_dotenv

load_dotenv()

def connection_database():
    """
        Cria e retorna uma conexão com o banco de dados
    """
    try:
        conn = psycopg.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            dbname=os.getenv('DB_NAME'),
            password=os.getenv('DB_PASSWORD'),
            user=os.getenv('DB_USER'),
            sslmode='require',
            channel_binding='require',
            row_factory=dict_row
        )

        return conn

    except psycopg.OperationalError:
        raise

    except Exception:
        raise

def test_connection():
    """
        Testa a conexão com o banco de dados executando uma query simples.
    """
    try:
        with connection_database() as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT 1;')

        print('Banco de dados conectado com sucesso.')

    except psycopg.Error as err:
        print(f'[Erro do BD]: Falha ao executar o comando SQL')
        print(f'Error: {err}')

    except Exception as err:
        print(f'Error: {err}')

if __name__ == '__main__':
    test_connection()
