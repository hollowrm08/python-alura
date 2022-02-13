import Programa


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome} | Ano: {self._ano} | Likes: {self._likes} | Duração: {self.__temporadas}'
