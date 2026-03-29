import psycopg2

def get_conn():
    return psycopg2.connect(
        dbname='incident',
        user='postgres',
        password='postgres',
        host='db'
    )

def init_db():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute('CREATE EXTENSION IF NOT EXISTS vector;')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS incidents (
                id SERIAL PRIMARY KEY,
                content TEXT,
                embedding VECTOR(384)
    );
    ''')

    conn.commit()
    conn.close()
    cur.close()