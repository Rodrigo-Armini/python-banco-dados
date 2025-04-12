from src.database.repositorios import produto_repositorio
import questionary


def executar_produto():
    opcoes = ["Listar todos", "Cadastrar", "Editar", "Apagar", "Voltar"]
    opcao_desejada = ""
    while opcao_desejada != "Voltar":
        opcao_desejada = questionary.select("Escolha o menu desejado dos produtos", opcoes).ask()
        if opcao_desejada == "Cadastrar":
             __cadastrar()    
        elif opcao_desejada == "Listar todos":
            __listar_todos()
        elif opcao_desejada == "Apagar":
            __apagar()
        elif opcao_desejada == "Editar":
            __editar()

def __editar():
    id_para_editar = int(questionary.text("Digite o id do produto para editar: ").ask())
    novo_nome_produto = questionary.text("Digite o nome do produto: ").ask()
    produto_repositorio.editar(id_para_editar, novo_nome_produto)
    print("Produto alterado com sucesso")

def __apagar():
    id_para_apagar = int(questionary.text("Digite o id do produto para apagar: ").ask())
    produto_repositorio.apagar(id_para_apagar)
    print("Produto apagado com sucesso")


def __listar_todos():
    produtos = produto_repositorio.listar_todos()
    print("Lista de produtos: ")
    for produto in produtos:
        print("Id:", produto["id"], "Nome:", produto["nome"])


# Funções com um/dois underline(s) antes do nome são consideradas
# funções privadas, ou seja, não devem/podem ser utilizadas em outros arquivos
def __cadastrar():
    # Função responsável por cadastrar um produto, solicitando os dados
    # necessários para o cadastro
    nome_produto = input("Digite o nome do produto: ")

    # Chamar a função de cadastrar(insert) o produto no bd
    # passando como parâmetro o nome do produto
    produto_repositorio.cadastrar(nome_produto)

    print("Produto cadastrado com sucesso")