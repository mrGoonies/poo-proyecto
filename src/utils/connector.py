"""Permite la conexión con la base de datos"""

import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

configuration: dict = {
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
}

def test_connection():
    try:
        connector = mysql.connector.connect(**configuration)
        cursor = connector.cursor()
        cursor.execute("SHOW DATABASES;")

        for query_result in cursor:
            print(query_result)
    
        return connector

    except Exception as error:
        print("Se a generado el siguiente error:\n{}".format(error))

def create_database_project(db_name) -> None:
    assert len(db_name) >= 3, "El largo del nombre es inválido. Debe tener un largo mínimo de 3 caracteres."

    connector = test_connection()
    cursor = connector.cursor()
    cursor.execute("CREATE DATABASE {}".format(db_name))

    print("La base de datos a sido creada correctamente con el siguiente nombre:\n{}".format(db_name))

def create_tables() -> None:
    pass



