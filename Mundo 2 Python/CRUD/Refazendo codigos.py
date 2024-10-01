import os
from dataclasses import dataclass
import time
os.system("cls||clear")

list_dados = []

def logo():
    print("""\033[34m
===============
---  \033[37mSENAI\033[34m  ---
===============  \033[m        

\n""") 

def criando_arquivo(a,b):
    with open(a,"a") as arquivo_dados:
        for dado in b:
            arquivo_dados.write(f"{dado.usuario}, {dado.senha}\n")
    arquivo_dados.close()
    print("\n=== Dados Salvos ===\n")

def lendo_arquivo(a):
    list_dados=[]
    with open(a,"r") as arquivo_origem:
        for linha in arquivo_origem:
            usuario, senha = linha.strip().split(",")
            list_dados.append(Dados(usuario=usuario, senha=int(senha)))
    arquivo_origem.close()
    return list_dados

@dataclass
class Dados:
    usuario : str
    senha : int


while True:
    while True:
        logo()
        print("=== BEM VINDO ===\n\n")
        opcao=int(input("""Informe a opção desejada: 
1- CRIAR LOGIN
2- EFETUAR LOGIN
3- EXCLUIR LOGIN
: """))
        match (opcao):
            case 1:
                list_dados = []
                print("\n=== CRIANDO LOGIN ===\n")
                dados = Dados(
                    usuario = input("Usuario: "),
                    senha = int(input("Senha: "))
                )
                list_dados.append(dados)
                login_senha = "login_senha.txt"
                criando_arquivo(login_senha,list_dados)
                opcao1 = 1
                if opcao1 == 1:
                    print("Login criado com sucesso.\nFaça login para ter acesso aos dados.")
                    time.sleep(3)
                    os.system("cls||clear")
                    opcao
                else: 
                    break             
            case 2:
                print("\n=== EFETUANDO LOGIN ===\n")
                login = input("Usuario: ")
                senha1 = int(input("Senha: "))
                login_senha = "login_senha.txt"
                list_dados=[]
                list_dados=lendo_arquivo(login_senha)
                for dados in list_dados:
                    if dados.usuario == login:
                        if dados.senha == senha1:
                            print("=== LOGIN EFETUADO ===")
                            time.sleep(5)
                            os.system("cls||clear")
                            break
                        else: 
                            print("Senha incorreta!")
                    else:
                        print("Login incorreto!")
            case 3:
                print("=== EM DESENVOLVIMENTO ===")