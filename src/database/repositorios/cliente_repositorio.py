from src.database.conexao import abrir_conexao


def cadastrar(nome_cliente: str, cpf_cliente: str):
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
        cursor.execute("insert into clientes (nome, cpf) values (%s, %s)", (nome_cliente,cpf_cliente))

        # Commit é necessário pois sem ele o insert n será concretizado no bd
        conexao.commit()
        # Fechar a conexão com o bd
        conexao.close()
        
    except Exception as e:
        print(e)

def listar_todos():
    try:
        conexao = abrir_conexao()
        cursor = conexao.cursor()
        cursor.execute("Select cpf, nome from clientes")
        registros = cursor.fetchall()

        clientes = []
        for registro in registros:
            cliente = {
                "cpf": registro[0],
                "nome": registro[1]
            }
            clientes.append(cliente)
        return clientes
    except Exception as er:
        print("Não foi possível carregar os clientes")
        print(er)

def editar(cpf_editar: int, nome: str):
    try:
        conexao = abrir_conexao()
        cursor = conexao_cursor()
        cursor.execute("update clientes set nome = %s where cpf = %s", (nome, cpf_editar))
        conexao.commit()
        conexao.close()
    except Exception as error:
        print("Não fo possível alterar o cliente")
        print(error)

def apagar(cpf_pagar: int):
    try: 
        conexao = abrir_conexao()
        cursor = conexao.cursor()
        cursor.execute("delete from clientes where cpf = %s", (cpf_pagar,))
        conexao.commit()
        conexao.close()
    except Exception as erro:
        print("Não foi possível apagar o registro")
        ptint(erro)