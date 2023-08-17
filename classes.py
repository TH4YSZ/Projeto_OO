import random
clientes = []
class Banco:
    def __init__(self):
        self._clientes = []
        self._nome = ("MMALT-PAY")
    
    conta = 0000
    def adicionar_cliente(self):
        self.nome = ""
        self.cpf = ""
        self.conta = conta + 1
        self.saldo = 0
        self.endereço = ""
        self.telefone = ""
        self.idade = ""
        self.email = ""
        self.senha = ""
    
    def setNome (self, nome):
        self.nome = nome

    def getNome (self):
        return self.nome 

    def setTelefone (self, telefone):
        self.telefone = telefone
    
    def getTelefone (self):
        return self.telefone 

    def setCPF(self, cpf):
        self.cpf = cpf
    
    def getCPF(self):
        return self.cpf 
        
        
    def cadastrar_cliente(self, nome, cpf, idade, telefone, email, senha):
        cliente = Cliente(nome, cpf, idade, telefone, email, senha)
        self.__clientes.append(cliente)
        
    def validar_cliente_por_cpf_e_senha(self, cpf, senha):
        for cliente in self._clientes:
            if cliente.get_cpf() == cpf and cliente.verificar_senha(senha):
                return cliente
            else:
                print("CPF ou senha incorreto.")
        

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
        Banco.validar_cliente_por_cpf_e_senha()

    


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
    def __init__(self, valor, cpf, senha, saldo, cliente_a, cliente_b):
        self._valor = valor
        self._cpf = cpf
        self._senha = senha
        self._clientes = []
        self._saldo = saldo
        self._cliente_b = cliente_b
        self._cliente_a = cliente_a
        
    

    def sacar(self, valor):
        if(self.__if_saque(valor)):
            self.__saldo -= valor

        else:
            print(f'o valor de {valor} passou o limite para saque')


    def depositar (self, valor, nome, cpf, saldo):
        if valor > 0:
            self.saldo += valor
            self.nome = nome
            self.cpf = cpf
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}") 

    def transferencia (self,valor,cliente_a, cliente_b,cpf, senha,saldo):
            cliente_a.saldo = cliente_a.depositar()
            cliente_b.saldo = cliente_b.depositar()
            
            cliente_a = Banco.validar_cliente_por_cpf_e_senha()

            if cpf and senha in clientes:
                cliente_b = int (input("Informe o CPF do destinatário",cpf))
                for cpf, in clientes:
                    valor = float (input("Informe a quantia que deseja transferir:"))
                    cliente_b.saldo = cliente_b.saldo + valor
                    cliente_a.saldo = cliente_a.saldo - valor
                    print ("Transferencia no valor de R$",valor, "concluída")
                else:
                    print ("Usuário não encontrado")
            else:
                print ("Usuário não encontrado")
            
