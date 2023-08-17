import random
cliente = []
class Banco:
    def __init__(self):
        self._clientes= []
    
    def adicionar_cliente(self, nome, cpf, idade, telefone, email, senha):
        numero_agencia = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        print ("O número da sua agência é:" (numero_agencia))
        
        parte_numerica = ''.join([str(random.randint(0, 9)) for _ in range(8)])
        digito_verificador = random.randint(0, 9)
        numero_conta = f"{parte_numerica}-{digito_verificador}"
        print ("O número da sua conta é:" (numero_conta))
        
        cliente = Banco({"Número da conta: ": numero_conta, "Agência:": numero_agencia, "Nome:": nome, "CPF": cpf, "Idade:" :idade,"Telefone:" :telefone,"Email:":email, "Senha:":senha})
        self._clientes.append(cliente)
        
        
    def validar_cliente_por_cpf_e_senha(self, cpf, senha):
        for cliente in self._clientes:
            if cliente.get_cpf() == cpf and cliente.verificar_senha(senha):
                return cliente
        return print("CPF ou senha incorreto.")

    def alterar_dados_cliente(self, cpf, senha, novo_nome, novo_email, novo_telefone, novo_cpf, nova_senha, nova_idade):
        cliente = self.validar_cliente_por_cpf_e_senha(cpf, senha)
        if cliente:
            cliente.set_nome(novo_nome)
            cliente.set_email(novo_email)
            cliente.set_telefone(novo_telefone)
            print("Dados do cliente alterados com sucesso!")
        else:
            print("Cliente não autenticado.")
        
    def excluir_conta(self, senha, cpf, clientes):
        for cpf in self._clientes:
            if cpf in clientes:
                if senha in clientes:
                    del clientes
                else:
                    print ("Senha Inválida")
        else:
            print("CPF Inválido")

    def excluirtitular (self, cpf):
        x = input ()
        titulares_removidos = [titular for titular in self._titulares if titular['CPF'] == cpf]
        if titulares_removidos:
            self.pessoas = [titular for titular in self._titulares if titular['CPF'] != cpf]
            print(f"{cpf} removido(a) da lista de pessoas.")
        else:
            print(f"Titular do CPF: {cpf} não encontrado(a) na lista do banco.")

    def alterar_conta(self, senha, cpf, clientes1):
        x = int (input("Cpf:"))
        y = int (input("Senha:"))
        if cpf in clientes1:
            if senha in clientes1:
                 clientes1
            else:
                print ("Senha Inválida")
        else:
            print("CPF Inválido")


# Menu inicial:

# Fazer login -> cpf e senha
# Criar conta -> nome, cpf, senha, data de nascimento
# Sair

# Menu depois de ter feito o login:

# Excluir Conta -> cpf e senha
# Alterar Conta -> O que você deseja alterar?  nome, cpf, senha, data de nascimento
# Depositar -> 
# Sacar 
# Transferir
# Sair
class Cliente:
    def __init__(self, valor, cliente_a, cliente_b, cpf, senha, saldo):
        self._valor = valor
        self._cliente_a = cliente_a
        self._cliente_b = cliente_b
        self._cpf = cpf
        self._senha = senha
        self.cliente = []
        self._saldo = saldo
    

    def sacar(self, valor):
        if(self.__if_saque(valor)):
            self.__saldo -= valor

        else:
            print(f'o valor de {valor} passou o limite para saque')


    def depositar (self, valor, nome, cpf):
        f valor > 0:
        self.saldo += valor
        self.nome = nome
        self.cpf = cpf
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}") 

    def transferencia (self,valor, cliente_b,cpf, senha,saldo):
            cliente_a.saldo = cliente_a.depositar()
            cliente_b.saldo = cliente_b.depositar()
            
            cliente_a = Banco.validar_cliente_por_cpf()
            cliente_a = Banco.validar_cliente_por_senha()
            if cpf and senha in cliente:
                cliente_b = int (input("Informe o CPF do destinatário",cpf))
                for cpf, in cliente:
                    valor = float (input("Informe a quantia que deseja transferir:"))
                    cliente_b.saldo = cliente_b.saldo + valor
                    cliente_a.saldo = cliente_a.saldo - valor
                    print ("Transferencia no valor de ",valor, "concluída")
                else:
                    print ("Usuário não encontrado")
            else:
                print ("Usuário não encontrado")
            
