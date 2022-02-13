class Conta:

    def __init__(self, numero, titular, saldo, limite=1000):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def imprimir_extrato(self):
        print(f'O saldo do titular "{self.__titular}" é: R$ {self.__saldo:.2f}')

    def sacar(self, valor):
        self.__saldo -= valor

    def depositar(self, valor):
        self.__saldo += valor

    def transferir(self, conta_destino, valor):
        self.sacar(valor),
        conta_destino.depositar(valor)
