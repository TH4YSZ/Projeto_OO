class banco:
    def __init__(self, nome, idade, telefone, email, cpf, senha):
        self._nome = nome
        self._idade = idade
        self._telefone = telefone
        self._email = email
        self._cpf = cpf
        self._senha = senha

    def cadastrar(self,_nome,_idade,_telefone,_email,_cpf, _senha):
        clientes = banco(_nome,_idade,_telefone, _email,_cpf,_senha)
