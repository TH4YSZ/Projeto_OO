from classe_cliente import*
import getpass
import os

def op_invalida():
    print("\n Opção inválida. \n")
    os.system("pause")
    os.system("cls")

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

                if trava == 1: #teste
                    print("Digite seu nome: ")
                    print("Digite sua senha")
            
            #Cadastro
            case 2:
                try:
                    trava = 1
                    os.system("cls")
                    print("Preencha as informações abaixo \n")
                    nome = input("Nome: ")
                    cpf = int(input("CPF: "))
                    idade = int(input("Idade: "))
                    telefone = input("Telefone: ")
                    email = input("Email: ")
                    senha = getpass.getpass("Digite sua senha: ")
                    banco.adicionar_cliente(nome, cpf, idade, telefone, email, senha)

                    if idade < 18:
                        print("\nDesculpe, você não pode ter uma conta se for menor de 18 anos.")
                        
                    else:
                        print("\nUsuário cadastrado com sucesso!")
                    op = int(input("\n [1] Voltar \n [2] Sair \n \nDigite a opção desejada: ")) #Opções para voltar/sair do software.

                    if op == 1: #Voltar
                        y = 0
    
                        os.system("cls")

                    elif op == 2: #Sair
                        y = 1
                      

                    else: #Opção inválida
                        op_invalida()
                           
                except Exception in erro:
                    op_invalida()
            case 3:
                y = 1
            
            case _:
                op_invalida()

    except Exception as erro:
        op_invalida()