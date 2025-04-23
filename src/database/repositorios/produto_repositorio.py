from typing import List
from src.database.conexao import abrir_conexao
from src.models.produto import Produto


def cadastrar(produto: Produto):
    try:
        conexao = abrir_conexao()
        
        # Criar um cursor que nos permitirá executar comandos no banco de dados
        cursor = conexao.cursor()
        
        # SQL Injection é uma técnica de ataque em que comandos SQL maliciosos são inseridos em entradas 
        # de dados para manipular o banco de dados. Em Python, proteger-se contra SQL Injection é 
        # essencial para evitar vazamento de dados e garantir a segurança de aplicativos web.
        # Como prevenir:
        # update colaboradores set nome = 'Francisco', idade = 31 where id = 10;
        # "update colaboradores set nome = %s, idade = %s where id = %s", (colaborador_nome, idade, id)
        
        # Definir qual será o comando que iremos executar, neste caso será um insert
        cursor.execute("insert into produtos (nome) values (%s)", (produto.nome,))

        # Commit é necessário pois sem ele o insert n será concretizado no bd
        conexao.commit()
        # Fechar a conexão com o bd
        conexao.close()
        
    except Exception as e:
        print(e)

def listar_todos() -> List[Produto]:
    try:
        # Abrir uma conexão com o banco de dados
        conexao = abrir_conexao()
        # Criar um cursor que nos permitirá executar comandos n banco de dados
        cursor = conexao.cursor()

        # Executar a consulta SQL para buscar todos os produtos (id e nome)
        cursor.execute("Select id, nome from produtos ORDER BY nome")
        registros = cursor.fetchall()

        produtos = []
        for registro in registros:


            produto = Produto(nome=registro[1], id=int(registro[0]))
            produtos.append(produto)
        return produtos
    except Exception as err:
        print("Não foi possível carregar os produtos")
        print(err)

def apagar(id_apagar: int):
    try:
        conexao = abrir_conexao()
        cursor = conexao.cursor()
        cursor.execute("delete from produtos where id = %s", (id_apagar,))
        conexao.commit()
        conexao.close()
    except Exception as er:
        print("Não foi possível apagar o registro")
        print(er)

def editar(produto: Produto):
    try:
        conexao = abrir_conexao()
        cursor = conexao.cursor()
        cursor.execute("update produtos set nome = %s where id = %s", (produto.nome, produto.id))
        conexao.commit()
        conexao.close()
    except Exception as error:
        print("Não foi possível alterar o produto")
        print(error)