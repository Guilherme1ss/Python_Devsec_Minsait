from banco import Banco
from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca

banco = Banco()
conta_corrente1 = ContaCorrente(
    id_conta=3, saldo=4000, limite=50, banco=banco, nome_do_usuario='Guilherme')
conta_corrente2 = ContaCorrente(
    id_conta=4, saldo=1000, limite=50, banco=banco, nome_do_usuario='Pedro')

# A conta poupança está sempre vinculada a uma conta corrente, a conta poupança deve NECESSARIAMENTE ter o mesmo id da conta corrente vinculada a ela, pois ambas devem ser do mesmo titular.
poupanca_guilherme = ContaPoupanca(
    id_conta=3, saldo=0, taxa_juros_anual=100, banco=banco)

# O deposito não é vinculado a conta corrente, diferente do saque.
poupanca_guilherme.depositar(valor=1000000000000)

# Insira o tempo que o seu dinheiro vai ficar na conta poupança e verifique o seu rendimento prevista. (OBS: essa função apenas verifica o rendimento futuro e NÂO o atualiza no self.saldo. Ela é apenas para consulta)
poupanca_guilherme.verificar_taxa_de_rendimento_ao_ano(
    segundos=0, minutos=0, horas=0, dias=0, meses=0, anos=1)

# Ao sacar o dinheiro da sua conta poupança ela vai diretamente para conta corrente de mesmo id.
poupanca_guilherme.sacar(valor= 600)

# Transfere dinheiro entre contas correntes
conta_corrente2.transferir(id_conta_destino=3, valor=1000)
conta_corrente2.transferir(id_conta_destino=3, valor=1000)

# Teste de depositos e saques.
conta_corrente1.sacar(700)
conta_corrente1.depositar(200)
conta_corrente1.sacar(5125)
conta_corrente1.sacar(100)
conta_corrente1.sacar(20)
conta_corrente1.depositar(50)
conta_corrente1.depositar(500)

# Exibe o extrato da conta corrente.
conta_corrente1.exibir_extrato()
