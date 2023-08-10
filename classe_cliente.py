class Cliente:
    def __init__(self, nome, telefone, email, senha):
        self.nome = nome
        self.senha = senha
        self.telefone = telefone
        self.email = email

class Banco:
    def __init__(self, nome):
        self.clientes = []

    def adicionar_cliente(self, nome, telefone, email, senha):
        cliente = Cliente(nome, telefone, email, senha)
        self.clientes.append(cliente)

