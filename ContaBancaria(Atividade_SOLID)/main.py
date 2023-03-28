from banco import Banco
from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca

banco = Banco()
conta_corrente1 = ContaCorrente(id_conta=3, saldo=4000, limite=50, banco= banco, nome_do_usuario= 'Guilherme')
conta_corrente2 = ContaCorrente(id_conta=4, saldo=1000, limite=50, banco= banco, nome_do_usuario= 'Pedro')

# A conta poupança está sempre vinculada a uma conta corrente, a conta poupança deve NECESSARIAMENTE ter o mesmo id da conta corrente vinculada a ela.
poupanca_guilherme = ContaPoupanca(id_conta= 3, saldo= 0, taxa_juros_anual=100, banco= banco)
poupanca_guilherme.depositar(valor=1000000000000)
poupanca_guilherme.verificar_taxa_de_rendimento_ao_ano(segundos=0, minutos=0, horas=0, dias= 0, meses= 0, anos= 1)


conta_corrente2.transferir(id_conta_destino=3, valor=1000)
conta_corrente2.transferir(id_conta_destino=3, valor=1000)


conta_corrente1.sacar(700)
conta_corrente1.depositar(200)
conta_corrente1.sacar(4525)
conta_corrente1.sacar(100)
conta_corrente1.sacar(20)
conta_corrente1.depositar(50)
conta_corrente1.depositar(500)
conta_corrente1.exibir_extrato()

