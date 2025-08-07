# db_config.py

import mysql.connector
from import Error

def conectar() 
    try:
        conexao = mysql.connector.connect(
            host= 'localhost',
            user='root'             #Troque se necessário
            passoword='eec123456@#$,'       # troque se necessário
            database='sfb' # Nome do seu banco
        )
        if conexao.is_connected():
            print("conexão bem-sucedida com o banco de dados!")
            return conexao
    except Error as e:
        print(f)