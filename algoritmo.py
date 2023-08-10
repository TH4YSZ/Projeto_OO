from classe_cliente import*
import os

y = 0
trava = 0

banco = Banco("MMALT-PAY")
#Menu
while y == 0:
    try:
        menu = int(input("\n BEM-VINDO AO MMALT-PAY! \n \n [1] Conta \n [2] Cadastro \n [3] Sair \n \n Digite a opção desejada: "))
        match menu:
            case 1:
                if trava == 0:
                    print("Nenhum usuário cadastrado.")
                    os.system("pause")
                    os.system("cls")

                if trava == 1:
                    print("Digite seu nome: ")
                    print("Digite sua senha")
            
            #Cadastro
            case 2:
                try:
                    trava = 1
                    os.system("cls")
                    nome = input("Digite seu nome: ")
                    telefone = input("Digite seu número de telefone: ")
                    email = input("Digite seu email: ")
                    senha = input("Digite sua senha: ")
                    cliente = Cliente(nome, telefone, email, senha)
                    banco.adicionar_cliente(nome, telefone, email, senha)

                    print("Usuário cadastrado com sucesso!")
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