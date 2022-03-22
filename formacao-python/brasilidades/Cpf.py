from validate_docbr import CPF


class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.validar_cpf(documento):
            self._cpf = documento
        else:
            raise ValueError("CPF não é válido!")

    def validar_cpf(self, documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError("Quantidade de dígitos invalida!")

    def __str__(self):
        return self.formatar_cpf()

    def formatar_cpf(self):
        mascara = CPF()
        return mascara.mask(self._cpf)
