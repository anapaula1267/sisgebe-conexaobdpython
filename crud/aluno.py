# crud_aluno.py
from db_config import conectar
from hashlib import sha256

def hash_senha(senha):
    return sha256(senha.encode('utf-8')).hexdigest()

def criar_aluno(name, senha, serie, status='ativo')
    try:
        conn = conectar()
        cursor = conn.cursor()
        senha_h = hash_senha(senha)
        cursor.execute(
            "INSERT INTO ALUNO (nome, email, senha, serie, status) VALUES (%s, %s, %s, %s, %s)",
            (nome, email, senha_h, serie, status)        
        )
        conn.commit()
        return{"status": "sucesso", "mensagem": "Aluno criado.", "id":cursor.lastrowid}
    except Exception as e:
        return{"status":"erro", "mensagem": str(e)}
    finally:
        try: conn.close()
        except: pass

def listar_alunos():
    try:
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.excute("")
        