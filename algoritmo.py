from classe_cliente import*
import os

y = 0


banco = Banco("MMALT-PAY")
#Menu
while y == 0:
    try:
        menu = int(input("\n BEM-VINDO AO MMALT-PAY! \n \n [1] Conta \n [2] Cadastro \n [3] Sair \n \n Digite a opção desejada: "))
        match menu:
            case 2:
                try:
                    os.system("cls")
                    nome = input("Digite nome e sobrenome: ")
                    telefone = input("Digite o número de telefone: ")
                    email = input("Digite o email: ")
                    senha = input("Digite a senha: ")
                    cliente = Cliente(nome, telefone, email, senha)
                    banco.adicionar_cliente(nome, telefone, email, senha)

                    print("Cliente cadastrado com sucesso!")
                    os.system("pause")
                    os.system("cls")
                except Exception in erro:
                    op_invalida()
            case 3:
                y = 1
            
            case _:
                op_invalida()

    except Exception as erro:
        op_invalida()

def op_invalida():
    print("\n Opção inválida. \n")
    os.system("pause")
    os.system("cls")