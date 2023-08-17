from classes import *
import getpass
import os

def op_invalida():
    print("\n Opção inválida. \n")
    os.system("pause")
    os.system("cls")

y = 0
trava = 0

#Menu
while y == 0:
    banco = Banco()
    cliente = Cliente()
    
    try:
        menu = int(input("\n BEM-VINDO AO MMALT-PAY! \n \n [1] Conta \n [2] Cadastro \n [3] Sair \n \n Digite a opção desejada: "))
        match menu:
            case 1:
                if trava == 0:
                    print("Nenhum usuário cadastrado.")
                    os.system("pause")
                    os.system("cls")

                if trava == 1: #teste
                    os.system("cls")
                    print("Preencha as informações para acessar sua conta. \n")
                    cpf = int(input("CPF: "))
                    senhaa = getpass.getpass("Digite sua senha: ")
                    cliente_encontrado = banco.validar_cliente_por_cpf_e_senha(cpf, senhaa)

                    if cliente_encontrado:
                        os.system("cls")
                        op = int(input("[1] Transferência \n [2] Depósito \n [3] Saque \n [4] Alterar dados \n [5] Excluir conta  \n [6] Voltar \n \n Digite a opção desejada: "))
                        match op:
                            case 1:
                                print("Lógica tranferência")
                                cliente.transferencia()
                            case 2:
                                print("Lógica depósito")
                                cliente.depositar()
                            case 3:
                                print("Lógica saque")
                                cliente.sacar()
                            case 4:
                                os.system("cls")
                                menu2 = int(input("\n O que você deseja alterar? \n \n [1] Nome \n [2] Email \n [3] Telefone \n [4] CPF \n [5] Senha \n [6] Idade \n \n Digite a opção desejada: "))
                                match menu2:
                                    case 1:
                                        novo_nome = input("Digite o novo nome: ")
                                        cliente.setNome(novo_nome)
                                    case 2:
                                        novo_email = input("Digite o novo email: ")
                                        cliente.setEmail(novo_email)
                                    case 3:
                                        novo_telefone = input("Digite o novo telefone: ")
                                        cliente.setTelefone(novo_telefone)
                                    case 4:   
                                        novo_cpf = input("Digite o novo CPF: ")
                                        cliente.setCPF(novo_cpf)
                                    case 5:
                                        nova_senha = input("Digite a nova senha: ")
                                        cliente.setSenha(nova_senha)
                                    case 6:
                                        nova_idade = input("Digite a nova idade: ")
                                        cliente.setIdade(nova_idade)
                        
                            case 5:
                                print("Lógica excluir conta")
                            case 6:
                                os.system("cls")
                            case _:
                                op_invalida()
                    else:
                        print("Cliente não encontrado.")
            
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
        print("\n Opção inválida. \n")
        os.system("pause")
        os.system("cls")

