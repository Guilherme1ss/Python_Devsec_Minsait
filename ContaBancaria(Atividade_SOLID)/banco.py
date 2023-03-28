class Banco:
    def __init__(self):
        # Inicia dicionário de contas correntes e poupanças
        self.contas_corrente = {}
        self.contas_poupanca = {}

    # Método para cadastrar conta corrente no dicionário
    def cadastrar_conta_corrente(self, conta, nome, tipo):
        self.contas_corrente[conta.id_conta] = [conta, nome, tipo]
        self.buscar_conta_corrente_por_id(conta.id_conta)

     # Método para cadastrar conta poupança no dicionário
    def cadastrar_conta_poupanca(self, conta, tipo):
        self.buscar_conta_corrente_por_id(conta.id_conta) # Busca se a existe uma conta corrente registrada com o mesmo id da conta poupança para vincular contas
        nome = self.contas_corrente[conta.id_conta][1] # Busca nome do usuário dono da conta poupança
        self.contas_poupanca[conta.id_conta] = [conta, nome, tipo] # Conta poupança vai possuir o mesmo usuário da conta corrente


    def buscar_conta_corrente_por_id(self, id_conta):
        conta = self.contas_corrente.get(id_conta)
        if not conta:
            raise ValueError(f"Conta com id {id_conta} não encontrada.")
        return conta

    def buscar_conta_poupanca_por_id(self, id_conta):
        conta = self.contas_poupanca.get(id_conta)
        if not conta:
            raise ValueError(f"Conta com id {id_conta} não encontrada.")
        return conta

    def buscar_nome_da_conta(self, id_conta_origem, id_conta_destino):
        nome_conta_origem = self.contas_corrente[id_conta_origem][1]
        nome_conta_destino = self.contas_corrente[id_conta_destino][1]
        return nome_conta_origem, nome_conta_destino

    def transferir_valor(self, id_conta_origem, id_conta_destino, valor):
        conta_origem = self.buscar_conta_corrente_por_id(id_conta_origem)
        conta_destino = self.buscar_conta_corrente_por_id(id_conta_destino)
        nome_conta_origem, nome_conta_destino = self.buscar_nome_da_conta(
            id_conta_origem=id_conta_origem, id_conta_destino=id_conta_destino)
        if conta_origem is not None and conta_destino is not None:
            if conta_origem[0].saldo >= valor:
                conta_origem[0].sacar(valor)
                conta_destino[0].depositar(valor)
                print(
                    f"Transferência de R${valor:.2f} da conta de {nome_conta_origem} para a conta de {nome_conta_destino} realizada com sucesso.")
            else:
                print("---------------------------------------------------------------")
                print(
                    f"Saldo insuficiente na conta de {nome_conta_origem} para realizar a transferência.\nNão é possível utilizar o limite da sua conta para transferências.")
                print("---------------------------------------------------------------")
        else:
            print("---------------------------------------------------------------")
            print("Não foi possível realizar a transferência.")
            print("---------------------------------------------------------------")

    def sacar_poupança_corrente(self, id_poupanca, valor):
        conta_poupanca = self.buscar_conta_poupanca_por_id(id_poupanca)
        conta_corrente = self.buscar_conta_corrente_por_id(id_poupanca)
        if self.validar_valor(conta_poupanca, valor) == True:
            conta_poupanca[0].atualizar_saldo_saque(valor)
            conta_corrente[0].depositar(valor)
        else:
            conta_poupanca[0].saldo_insuficiente(valor=valor)

    def validar_valor(self, conta_poupanca, valor):
        if conta_poupanca[0].saldo >= valor:
            return True
        else:
            return False

    def validar_poupanca(self, conta_id):
        if conta_id in self.contas_corrente:
            print(
                f'Conta poupança vinculada a conta corrente de id {conta_id}')
        else:
            raise ValueError(
                'É necessário possuir uma conta corrente antes de criar a conta poupança.\n(A conta corrente e a conta poupança devem possuir o mesmo id.)')
