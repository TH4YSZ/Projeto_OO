cliente = []
class Banco:
    def __init__(self):
        self._clientes= []
    
    def adicionar_cliente(self, nome, cpf, idade, telefone, email, senha):
        cliente = Banco(nome, cpf, idade, telefone, email, senha)
        self._clientes.append(cliente)
        
    def validar_cliente_por_cpf(self, cpf):
        for cliente in self.clientes:
            if cliente.get_cpf() == cpf:
                return cliente
        return ("CPF não encontrado.")

    def validar_cliente_por_senha(self, senha):
        for cliente in self.clientes:
            if cliente.get_senha() == cpf:
                return cliente
        return ("Senha incorreta")

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
    def __init__(self, valor, cliente_a, cliente_b, cpf, senha):
        self._valor = valor
        self._cliente_a = cliente_a
        self._cliente_b = cliente_b
        self._cpf = cpf
        self._senha = senha
        self.cliente = []
    
    def transferencia (self,valor, cliente_a, cliente_b, cpf, senha):
        Banco.validar_cliente_por_cpf()
        Banco.
        cliente_a = int(input("Informe seu CPF:", cpf))
        if cpf in cliente:
            cliente_a = int (input("Informe sua senha:",senha))
            if cpf and senha in cliente:
                cliente_b = int (input("Informe o CPF do destinatário",cpf))
                for cliente_b, in cliente

        
        else:
            print ("Usuário não encontrado")
        

    def sacar(self, valor):
        if(self.__if_saque(valor)):
            self.__saldo -= valor

        else:
            print(f'o valor de {valor} passou o limite para saque')


    def depositar (self, valor, nome, cpf):
        f valor > 0:
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

