fro db_config import conectar
 cria
def criar_categoria(nome,descricao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Categoria (nome, descricao)VALUES(%s, %s)", (nome, descricao))
    conn.commit()
    conn.close()
    print("categoria criada com sucesso!")

def listar_categoria(nome, descricao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT *FROM Categoria")
    caregoria = cursor.fetchall()
    conn.close()
    return categorias

def atualizar_categoria(id_categoria, novo_nome, nova_descricao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE categoria SET nome=%s, descricao=%s where id=%s",
                    (novo_nome, nova_descricao, id_categoria))
    conn.commit()
    conn.close()
    print("categoria atualizada")

    def deletar_categoria(id_categoria):