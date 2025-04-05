from mysql.connector import connect 

if __name__ == "__main__":
    print("tentando conectar no banco de dados")

    conexao = connect(
        host="127.0.0.1", # host é a máquina que está o banco de dados
        port=3306, # porta padrão do MySQL
        user="root",
        password="admin",
        database="super_empresa"
    )
    print("Conexão realizada com sucesso")
    # Criar um cursor que nos permitirá executar comandos no banco de dados
    cursor = conexao.cursor()
    # Definir qual será o comando que iremos executar, neste caso será um insert
    cursor.execute("insert into produtos (nome) values ('X-calabresa')")

    # Commit é necessário pois sem ele o insert não será concretizado no bd
    conexao.commit()
    # Fechar a conexao com o bd
    conexao.close()
    print("Produto cadastrado com sucesso")