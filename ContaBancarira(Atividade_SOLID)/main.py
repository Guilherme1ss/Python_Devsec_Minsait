from typing import Union
from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca

def exibir_saldo(conta: Union[ContaCorrente, ContaPoupanca]) -> None:
    if isinstance(conta, ContaCorrente):
        print("---------------------------------------------------------------")
        print(f"Saldo atual da conta corrente: R${conta.saldo:.2f} + Limite da conta: R${conta.limite_atual:.2f}")
        print("---------------------------------------------------------------")
    else: 
        print("---------------------------------------------------------------")
        print(f"O saldo atual da conta poupança é: R${conta.saldo:.2f}")
        print("---------------------------------------------------------------")


conta_corrente = ContaCorrente(id_conta=1, saldo=100, limite=50)
exibir_saldo(conta_corrente)
conta_corrente.sacar(700)
exibir_saldo(conta_corrente) # 0, 50
conta_corrente.depositar(200)
exibir_saldo(conta_corrente) # 50, 50
conta_corrente.sacar(350)
exibir_saldo(conta_corrente) # 0, 0
conta_corrente.depositar(50)
exibir_saldo(conta_corrente) # 50, 50


# Criando uma instância da classe ContaPoupanca
poupanca = ContaPoupanca(id_conta= 1, saldo= 0, taxa_juros_anual=100)

# Realizando um depósito na conta poupança
poupanca.depositar(valor=1000, meses=8)

# Verificando o saldo atual da conta poupança
exibir_saldo(poupanca)

# Realizando um saque na conta poupança
poupanca.sacar(250)

# Verificando o saldo atual da conta poupança após o saque
exibir_saldo(poupanca)


# Verificando o saldo atual da conta poupança após o resgate
exibir_saldo(poupanca)
