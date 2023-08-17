class Cliente:
    def __init__(self, nome, cpf, idade, telefone, email, senha):
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade
        self.__telefone = telefone
        self.__email = email
        self.__senha = senha
        self.__saldo = 0.0

    #Métodos getters
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
    
    def get_senha(self):
        return self.senha

    def get_saldo(self):
        return self.__saldo
    
    #Métodos setters
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    def set_idade(self, nova_idade):
        self.__idade = nova_idade

    def set_telefone(self, novo_telefone):
        self.__telefone = novo_telefone

    def set_email(self, novo_email):
        self.__email = novo_email

    def set_senha(self, nova_senha):
        self.__senha = nova_senha

