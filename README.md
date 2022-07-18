# Conta_Bancaria
O intuito é criar uma agencia de banco onde o usuário vai estar realizando transações como depositar, sacar e tranferir saldo da sua conta.

Foi criada um classe Pessoa, que vai ter funções como nome e idade.
Em seguida foi criado uma classe Cliente, a qual vai herdar Pessoa e ter uma função nome.
Criado classes da conta, se caso for conta poupança não vai poder sacar quando a conta estiver zerada, mas se for conta corrente o cliente pode sacar o saldo mais o limite.
Criado uma classe Banco, que vai gerenciar os acessos, caso agencia não existir no banco de dados vai aparecer uma mensagem que usuário não é autenticado.
