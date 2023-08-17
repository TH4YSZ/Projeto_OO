class Banco:
    def __init__(self, nome, idade, telefone, email, cpf, senha):
        self._nome = nome
        self._idade = idade
        self._telefone = telefone
        self._email = email
        self._cpf = cpf
        self._senha = senha
        self.clientes= []
        
    def cadastrar(self,nome,idade,telefone,email,cpf, senha):
        
        print("Para cadastrar um cliente, preencha as informações.")
        print()
        self.clientes = input([Banco( "Nome:",nome,"Idade:",idade,"Telefone:",telefone,"Email:", email,"CPF:",cpf, "Senha:",senha)])
        return self.clientes
    
    def adicionar_cliente(self, nome, cpf, idade, telefone, email, senha):
        cliente = Cliente(nome, cpf, idade, telefone, email, senha)
        self.__clientes.append(cliente)

    def adicionartitular (self, nometitular, senha, cpf, datadenasci):
        titular = ({"Nome:" : nometitular, "Senha:": senha, "CPF:" : cpf, "Data de Nascimento:": datadenasci})
        self._titulares.append (titular)
        print(f"{nometitular} adicionado(a) ao banco.")


    def excluir_conta(self,senha,cpf, clientes):
        print ("Para excluir sua conta, preencha as seguintes informações:")
        x = int (input("Cpf:"))
        y = int (input("Senha:"))
        if cpf in clientes:
            if senha in clientes:
                del clientes
            else:
                print ("Senha Inválida")
        else:
            print("CPF Inválido")

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


class Banco:

    def __init__(self):
        self._titulares = []

    def adicionartitular (self, nometitular, senha, cpf, datadenasci):
        titular = ({"Nome:" : nometitular, "Senha:": senha, "CPF:" : cpf, "Data de Nascimento:": datadenasci})
        self._titulares.append (titular)
        print(f"{nometitular} adicionado(a) ao banco.")
    
    def excluirtitular (self, cpf):
        titulares_removidos = [titular for titular in self._titulares if titular['CPF'] == cpf]
        if titulares_removidos:
            self.pessoas = [titular for titular in self._titulares if titular['CPF'] != cpf]
            print(f"{cpf} removido(a) da lista de pessoas.")
        else:
            print(f"Titular do CPF: {cpf} não encontrado(a) na lista do banco.")


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