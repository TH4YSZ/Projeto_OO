class Cliente:
    def __init__(self, nome, cpf, idade, telefone, email, senha):
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade
        self.__telefone = telefone
        self.__email = email
        self.__senha = senha
        self.__saldo = 0.0

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_idade(self):
        return self.__idade

    def get_telefone(self):
        return self.__telefone

    def get_email(self):
        return self.__email

    def get_saldo(self):
        return self.__saldo

class Banco:
    def __init__(self, nome):
        self.clientes = []

    def adicionar_cliente(self, nome, cpf, idade, telefone, email, senha):
        cliente = Cliente(nome, cpf, idade, telefone, email, senha)
        self.__clientes.append(cliente)

