from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca

conta_corrente = ContaCorrente(id_conta=1, saldo=100, limite=50)
conta_corrente.sacar(700) # 0, 50
conta_corrente.depositar(200) # 50, 50
conta_corrente.sacar(350) # 0, 0
conta_corrente.depositar(50) # 50, 50

# Criando uma instância da classe ContaPoupanca
poupanca = ContaPoupanca(id_conta= 1, saldo= 0, taxa_juros_anual=100)

# Realizando um depósito na conta poupança
poupanca.depositar(valor=1000, anos= 1)

# Realizando um saque na conta poupança
poupanca.sacar(250)
