from banco import Banco
from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca

banco = Banco()
conta_corrente1 = ContaCorrente(id_conta=3, saldo=4000, limite=50, banco= banco, nome_do_usuario= 'Guilherme')
conta_corrente2 = ContaCorrente(id_conta=4, saldo=1000, limite=50, banco= banco, nome_do_usuario= 'Pedro')


banco.transferir_valor(id_conta_origem=4, id_conta_destino=3, valor=1000)

'''
conta_corrente1.sacar(700)
conta_corrente1.depositar(200)
conta_corrente1.sacar(50)
conta_corrente1.sacar(280)
conta_corrente1.sacar(15)
conta_corrente1.depositar(50)
conta_corrente1.exibir_extrato()

# Criando uma instância da classe ContaPoupanca
poupanca = ContaPoupanca(id_conta= 1, saldo= 0, taxa_juros_anual=100)

# Realizando um depósito na conta poupança
poupanca.depositar(valor=1000, anos= 1)

# Realizando um saque na conta poupança
poupanca.sacar(250)
'''
