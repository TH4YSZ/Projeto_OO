import random
clientes = []
conta = 0000
class Banco:
    def __init__(self):
        self._clientes = []
        self._nome = ("MMALT-PAY")
    
    def adicionar_cliente(self):
        self._nome = ""
        self._cpf = ""
        self._conta = conta + 1
        self._saldo = 0
        self._endereço = ""
        self._telefone = ""
        self._idade = ""
        self._email = ""
        self._senha = ""
        clientes.append = [{"N° da conta:": self._conta, "Nome:": self._nome, "CPF:":self._cpf, "Endereço:": self._endereço, "Telefone:": self._telefone, "Idade:": self._idade, "Email": self._email, "Senha:":self._senha }]

    def setNome (self, nome):
        self._nome = nome

    def getNome (self):
        return self._nome 

    def setTelefone (self, telefone):
        self._telefone = telefone
    
    def getTelefone (self):
        return self._telefone 

    def setCPF(self, cpf):
        self._cpf = cpf
    
    def getCPF(self):
        return self._cpf 

    def setSenha(self, senha):
        self._senha = senha
    
    def setEmail(self, email):
        self._email = email
    
    def getEmail(self):
        return self._email
    
    def setIdade(self, idade):
        self._idade = idade
    
    def getIdade(self):
        return self._idade

    def setEndereço(self, endereço):
        self.endereço = endereço
    
    def getEndereço(self):
        return self.endereço

        
    def validar_cliente_por_cpf_e_senha(self, cpf, senha):
        for cliente in self._clientes:
            if cliente.getCPF() == cpf and cliente.verificar_senha(senha):
                return cliente
            else:
                print("CPF ou senha incorreto.")
        
    def excluir_conta(self):
        del self
        print("Cliente excluído com sucesso.")

    
class Cliente:
    def __init__(self, valor, cpf, senha, saldo, cliente_a, cliente_b):
        self._valor = valor
        self._cpf = cpf
        self._senha = senha
        self._clientes = []
        self._saldo = saldo
        self._cliente_b = cliente_b
        self._cliente_a = cliente_a

    def SetValor(self, valor):
        self._valor = valor

    def GetValor(self):
        return self._valor
       
    def SetCpf(self, cpf):
        self._cpf = cpf

    def GetCpf(self):
        return self._cpf

    def SetSenha(self, senha):
        self._senha = senha

    def GetSenha(self):
        return self._senha

    def SetSaldo(self, saldo):
        self._saldo = saldo

    def GetSaldo(self):
        return self._saldo

    def SetCliente_a(self, cliente_a):
        self._cliente_a = cliente_a

    def GetCliente_a(self):
        return self._cliente_a

    def SetCliente_a(self, cliente_b):
        self._cliente_b = cliente_b

    def GetCliente_b(self):
        return self._cliente_b
 

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
            
