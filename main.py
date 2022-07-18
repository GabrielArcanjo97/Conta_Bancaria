from cliente import Cliente
from banco import Banco
from tipo_conta import ContaCorrente, ContaPoupanca

banco = Banco()
cliente1 = Cliente('Gabriel', 25)
cliente2 = Cliente('Luana', 26)
cliente3 = Cliente('Josué', 24)

conta1 = ContaPoupanca(1111, 32587, 0)
conta2 = ContaCorrente(1111, 32588, 0, 100)
conta3 = ContaPoupanca(1111, 32587, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(20)
    cliente1.conta.sacar(10)
else:
    print('Cliente não autenticado.')

print('**************************')

if banco.autenticar(cliente2):
    cliente2.conta.depositar(20)
    cliente2.conta.sacar(10)
else:
    print('Cliente não autenticado.')










