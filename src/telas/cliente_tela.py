
import questionary
from src.database.repositorios import cliente_repositorio

def executar_cliente():
    opcoes = ["Listar todos", "Cadastrar", "Editar", "Apagar", "Voltar"]
    opcao_desejada = ""
    while opcao_desejada != "Voltar":
        opcao_desejada = questionary.select("Escolha o menu desejado dos clientes", opcoes).ask()
        if opcao_desejada == "Cadastrar":
            __cadastrar()
        elif opcao_desejada == "Listar todos":
            __listar_todos()
        elif opcao_desejada == "Apagar":
            __apagar()
        elif opcao_desejada == "Editar":
            __editar()

def __cadastrar():
    nome_cliente = input("Digite o nome do cliente: ")

    cpf_cliente = input("Digite o cpf do cliente: ")

    cliente_repositorio.cadastrar(nome_cliente, cpf_cliente)

    print("Cliente cadastrado com sucesso.")

def __editar():
    cpf_para_editar = int(questionary.text("Digite o cpf do cliente para editar: ").ask())
    novo_nome_cliente = questionary.text("Digite o nome do cliente: ").ask()
    cliente_repositorio.editar(cpf_para_editar, novo_nome_cliente)
    print("Cliente alterado com sucesso")

def __apagar():
    cpf_para_apagar = int(questionary.text("Digite o cpf do cliente para apagar: ").ask())
    cliente_repositorio.apagar(cpf_para_apagar)
    print("Cliente apagado com sucesso")

def __listar_todos():
    clientes = cliente_repositorio.listar_todos()
    print("Lista de clientes: ")
    for cliente in clientes:
        print("CPF:", cliente["cpf"], "Nome:", cliente["nome"])