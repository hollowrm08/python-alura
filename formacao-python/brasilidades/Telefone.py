import re


class Telefone:

    padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"

    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self._numero = telefone
        else:
            raise ValueError("Número Incorreto!")

    def __str__(self):
        return self.format_numero()

    def valida_telefone(self, telefone):

        resposta = re.findall(self.padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def format_numero(self):
        resposta = re.search(self.padrao, self._numero)
        return f'+{resposta.group(1)} ({resposta.group(2)}) {resposta.group(3)}-{resposta.group(4)}'
