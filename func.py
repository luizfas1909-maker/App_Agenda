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


garantir_tabela_compromissos()
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


garantir_tabela_compromissos()
from datetime import date

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


def converter_data_iso(data_texto):
    ano, mes, dia = map(int, data_texto.split("-"))
    return date(ano, mes, dia)


garantir_tabela_compromissos()
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
    print(f"Compromisso {nome} adicionado com sucesso")


def remover_compromisso(id):
    cursor.execute("DELETE FROM compromissos WHERE id = %s", (id,))
    conn.commit()
    print(f"Compromisso {id} removido com sucesso")


def listar_compromissos():
    cursor.execute("SELECT * FROM compromissos ORDER BY id")
    compromissos = cursor.fetchall()

    if not compromissos:
        print("Nenhum compromisso cadastrado.")
        return

    for compromisso in compromissos:
        print(
            f"ID: {compromisso[0]}, Nome: {compromisso[1]}, "
            f"Descricao: {compromisso[2]}, Data Limite: {compromisso[3]}"
        )


def atualizar_compromisso(id, nome, descricao, data_limite):
    cursor.execute(
        "UPDATE compromissos SET nome = %s, descricao = %s, data_limite = %s WHERE id = %s",
        (nome, descricao, data_limite, id),
    )
    conn.commit()
    print(f"Compromisso {id} atualizado com sucesso")


garantir_tabela_compromissos()
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="agendador",
    user="postgres",
    password="123456",
)
cursor = conn.cursor()


def adicionar_compromisso(nome, descricao, data_limite):
    cursor.execute(
        "INSERT INTO compromissos (nome, descricao, data_limite) VALUES (%s, %s, %s)",
        (nome, descricao, data_limite),
    )
    conn.commit()
    print(f"Compromisso {nome} adicionado com sucesso")


def remover_compromisso(id):
    cursor.execute("DELETE FROM compromissos WHERE id = %s", (id,))
    conn.commit()
    print(f"Compromisso {id} removido com sucesso")


def listar_compromissos():
    cursor.execute("SELECT * FROM compromissos")
    compromissos = cursor.fetchall()
    for compromisso in compromissos:
        print(
            f"ID: {compromisso[0]}, Nome: {compromisso[1]}, "
            f"Descricao: {compromisso[2]}, Data Limite: {compromisso[3]}"
        )


def atualizar_compromisso(id, nome, descricao, data_limite):
    cursor.execute(
        "UPDATE compromissos SET nome = %s, descricao = %s, data_limite = %s WHERE id = %s",
        (nome, descricao, data_limite, id),
    )
    conn.commit()
    print(f"Compromisso {id} atualizado com sucesso")
import psycopg2

conn = psycopg2.connect(
    host='localhost',	
    port='5432',
    database='agendador',
    user='postgres',
    password='123456'
)
cursor = conn.cursor()

def adicionar_compromisso(nome, descricao, data_limite):
    cursor.execute("INSERT INTO compromissos (nome, descricao, data_limite) VALUES (%s, %s, %s)", (nome, descricao, data_limite))
    conn.commit()
    print(f"Compromisso {nome} adicionado com sucesso")

def remover_compromisso(id):
    cursor.execute("DELETE FROM compromissos WHERE id = %s", (id,))
    conn.commit()
    print(f"Compromisso {id} removido com sucesso")
def listar_compromissos():
    cursor.execute("SELECT * FROM compromissos")
    compromissos = cursor.fetchall()
    for compromisso in compromissos:
        print(f"ID: {compromisso[0]}, Nome: {compromisso[1]}, Descrição: {compromisso[2]}, Data Limite: {compromisso[3]}")

def atualizar_compromisso(id, nome, descricao, data_limite):
    cursor.execute("UPDATE compromissos SET nome = %s, descricao = %s, data_limite = %s WHERE id = %s", (nome, descricao, data_limite, id))
    conn.commit()
    print(f"Compromisso {id} atualizado com sucesso")