import os

import questionary

from src.telas.cliente_tela import executar_cliente
from src.telas.produto_tela import executar_produto

if __name__ == "__main__":
    os.system("cls") # Limpar a tela
    opcoes = ["Clientes", "Produtos", "Sair"] # Lista de opções para o usuário
    opcao_desejada = ""
    while opcao_desejada != "Sair":
        opcao_desejada = questionary.select("Escolha o menu desejado", opcoes).ask()

        if opcao_desejada == "Produtos":
            executar_produto()
        
        elif opcao_desejada == "Clientes":
            executar_cliente()