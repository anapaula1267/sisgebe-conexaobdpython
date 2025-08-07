# app,py

from db_config import conectar

def main() -> None:
    conexao = conectar
    if conexao:
        try:
            cursor = conexao.cursor ()
            cursor.execute("SELECT * FROM livros;") # exemplo de consulta simples

            resultados = cursor.fet

            print("\nLivros cadastrados")
            for linha in resultados:
                print(linha)

        except Exception as e:
            print(f"Erro na execução: {e}")
        finally:
            conexao.close()
            print("\nConexão encerrada.")
            
if __name__ == "__main__":
    main()