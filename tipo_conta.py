from conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, valor):
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


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite = 100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Digite um valor numérico.')
        if valor <= 0:
            print('Digite um valor acima de zero.')
            return
        if (self.saldo + self.limite) < valor:
            print('Salfo insuficiente.')
            return
        self.saldo -= valor
        self.detalhes()

    def tranferir(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Digite um valor numérico.')
        if valor <= 0:
            print('Digite um valor acima de zero.')
            return
        if self.saldo < valor & self.limite > 0:
            print('Saldo insuficiente, você só tem valor do limite a ser sacado.')
            return
        self.saldo -= valor
        self.detalhes()
