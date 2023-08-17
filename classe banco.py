class Banco:
    def __init__(self, nome, idade, telefone, email, cpf, senha):
        self._nome = nome
        self._idade = idade
        self._telefone = telefone
        self._email = email
        self._cpf = cpf
        self._senha = senha
        self.clientes={}
        
    def cadastrar(self,nome,idade,telefone,email,cpf, senha):
        
        print("Para cadastrar um cliente, preencha as informações.")
        print()
        self.clientes = input({Banco( "Nome:",nome,"Idade:",idade,"Telefone:",telefone,"Email:", email,"CPF:",cpf, "Senha:",senha)})
        return self.clientes
    
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