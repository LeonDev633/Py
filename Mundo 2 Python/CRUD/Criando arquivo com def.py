import os
from dataclasses import dataclass
os.system("cls||clear")




@dataclass
class Dados:
    nome : str
    idade : int
    dinheiro : float
    altura : float
    peso : float

lista_dados = []

while True:
    opcao = int(input("Deseja Adicionar outra pessoa ? \n1-SIM\n2-NÂO"))
    if opcao == 2:
        break
    else:
        dados = Dados(
            nome = input("Nome: "),
            idade = int(input("Idade: ")),
            dinheiro = float(input("Valor: ")),
            altura = float(input("Altura")),
            peso = float(input("Peso: "))
        )
        lista_dados.append(dados)

#Exibindo dados:

            
arquivo_pgm_banco = "Arquivo Login e Senha.txt"

def criando_arquivo(a,b):
    with open(a,"a") as arquivo_dados:
        for item in b:
            arquivo_dados.write(f"{item.nome}, {item.idade}, {item.dinheiro}, {item.altura}, {item.peso}")
    print("\n=== Dados Salvos ===\n")
    
criador = criando_arquivo(arquivo_pgm_banco,lista_dados)

for item in lista_dados:
    print(f"Nome: {item.nome}")
    print(f"Idade: {item.idade}")
    print(f"Valor: {item.dinheiro}")
    print(f"Altura: {item.altura}")
    print(f"Peso: {item.peso}")