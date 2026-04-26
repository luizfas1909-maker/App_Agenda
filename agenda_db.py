import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="agendador",
    user="postgres",
    password="123456",
)
cursor = conn.cursor()


def garantir_tabela_compromissos():
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS compromissos (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(150) NOT NULL,
            descricao TEXT,
            data_limite DATE NOT NULL
        )
        """
    )
    conn.commit()


def adicionar_compromisso(nome, descricao, data_limite):
    cursor.execute(
        "INSERT INTO compromissos (nome, descricao, data_limite) VALUES (%s, %s, %s)",
        (nome, descricao, data_limite),
    )
    conn.commit()


def remover_compromisso(compromisso_id):
    cursor.execute("DELETE FROM compromissos WHERE id = %s", (compromisso_id,))
    reordenar_ids_compromissos()
    conn.commit()


def listar_compromissos():
    cursor.execute(
        "SELECT id, nome, descricao, data_limite FROM compromissos ORDER BY data_limite, id"
    )
    return cursor.fetchall()


def atualizar_compromisso(compromisso_id, nome, descricao, data_limite):
    cursor.execute(
        "UPDATE compromissos SET nome = %s, descricao = %s, data_limite = %s WHERE id = %s",
        (nome, descricao, data_limite, compromisso_id),
    )
    conn.commit()


def reordenar_ids_compromissos():
    cursor.execute(
        """
        WITH ordenados AS (
            SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS novo_id
            FROM compromissos
        )
        UPDATE compromissos c
        SET id = o.novo_id
        FROM ordenados o
        WHERE c.id = o.id
        """
    )
    cursor.execute(
        """
        SELECT setval(
            pg_get_serial_sequence('compromissos', 'id'),
            COALESCE((SELECT MAX(id) FROM compromissos), 0) + 1,
            false
        )
        """
    )


garantir_tabela_compromissos()
