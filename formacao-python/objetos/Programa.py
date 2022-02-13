class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f'Nome: {self._nome} | Ano: {self._ano} | Likes: {self._likes}'
