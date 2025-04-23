from typing import Optional


class Pessoa:
    """
    Classe Pessoa representa um humano, com nome e idade.
    """

    def __init__(self, nome: str, idade: int, nacionalidade: str = "Brasileiro", apelido: Optional[str] = None):
        """
        Construtor da classe.
        É chamado automaticamente quando for instanciado um objeto da classe Pessoa.

        Parêmetros:
        - nome: nome da pessoa do tipo string
        - idade: idade da pessoa do tipo inteiro
        - nacionalidade: nacionalidade da pessoa, é um parâmetro opcional que tem como valor default(padrão) None, ou seja,
        não preenchido
        """
        # self.nome, self.idade, self.nacionalidade, self.apelido e self.estudando são atributos da instância
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade
        self.apelido = apelido
        self.estudando = True 

    def __str__(self) -> str:
        """
        Representação informal do objeto, usada por print().
        Ex.: print(jose) -> Será apresentado os dados do cliente, não todos, os mais importantes
        """
        # return self.nome + " tem " + str(self.idade) + " anos de idade de nacionalidade " + self.nacionalidade + "."
        return f"{self.nome} tem {self.idade} anos de idade de nacionalidade {self.nacionalidade}."
    
    def fazer_aniversario(self):
        """
        Método utilizado para incrmentar a variável da idade em 1, será utilizado quando a pessoa fazer aniversário,
        para atualizar sua idade
        """
        self.idade = self.idade + 1

    def eh_adulto(self) -> bool:
        """
        Método com retorno do tipo boolean, para saber quando a pessoa é adulta ou não.
        Pessoas com idade supeior ou igual a 18 anos retornará true, caso contrário retornará false.
        """
        if self.idade > 17:
            return True
        else:
            return False
    
# instanciando um objeto chamado jose da classe Pessoa
jose = Pessoa(nome="José", idade=30, nacionalidade="Americano", apelido="Zeh")
patrick = Pessoa(nome="Ptarick", idade=18)
   
# chamando um método 'fazer_aniversario' do objeto patrick (da classe Pessoa)
patrick.fazer_aniversario()

print(patrick)
print(f"Patrick é adulto? {patrick.eh_adulto()}")