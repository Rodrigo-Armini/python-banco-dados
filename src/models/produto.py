from typing import Optional


class Produto:
    # __init__ é método construtor de uma classe Python
    def __init__(self, nome: str, id: Optional[int] = None):
        self.nome = nome
        self.id = id

