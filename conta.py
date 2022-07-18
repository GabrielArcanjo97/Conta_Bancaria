from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Digite um valor numérico.')
        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Digite um valor numérico.')
        if valor <= 0:
            print('Digite um valor acima de zero.')
            return
        self.saldo += valor
        self.detalhes()

    def tranferir(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Digite um valor numérico.')
        if valor <= 0:
            print('Digite um valor acima de zero.')
            return
        if self.saldo < valor:
            print('Saldo insuficiente.')
            return
        self.saldo -= valor
        self.detalhes()

    def detalhes(self):
        print(f'Agencia: {self.agencia}', end=' ')
        print(f'Conta: {self.conta}', end=' ')
        print(f'Saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor):
        pass