class BuscaEndereco:

    def __init__(self, cep):
        if self.verifica_cep(cep):
            self._cep = cep
        else:
            raise ValueError("CEP inválido!")

    def __str__(self):
        return self.format()

    def verifica_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format(self):
        return f'{self._cep[:5]}-{self._cep[5:]}'
