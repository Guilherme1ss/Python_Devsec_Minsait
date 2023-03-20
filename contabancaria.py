class ContaBancaria:
    def __init__ (self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar (self, valor):
        self.saldo += valor
        print('-------------------------------------------------------')
        print(f'Foi depositado o valor de R${valor:.2f} na sua conta.')
        print('-------------------------------------------------------')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print('-------------------------------------------------------')
            print(f'Valor de R${valor:.2f} foi sacado com sucesso')
            print('-------------------------------------------------------')
        else:
            print('-------------------------------------------------------')
            print('Saldo insuficiente')
            print('-------------------------------------------------------')
            
    def consultar_saldo(self):
        print('-------------------------------------------------------')
        print(f'Olá {self.titular}!\nO seu saldo atual é: R${self.saldo:.2f}')
        print('-------------------------------------------------------')
    

conta = ContaBancaria('Guilherme', 1000)
conta.consultar_saldo()
conta.sacar(500)
conta.depositar(1000)
conta.consultar_saldo()
conta.sacar(2000)