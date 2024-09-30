import os
os.system("cls||clear")
from dataclasses import dataclass
    
#Estrutura de dados:
@dataclass
class Carteira:
    nome : str
    notas : float
    moedas : float

lista_carteira=[]
QTD = 1
for i in range (QTD):
    carteira=Carteira(
        nome = input("Informe seu nome: "),
        notas =float(input("valor em notas: ")),
        idade=float(input("valor moedas: "))
    )
    lista_carteira.append(carteira)

for item in lista_carteira:
    print(f"{item.nome}")
    print(f"{item.notas}")
    print(f"{item.moedas}")

"""def salvando (a):
    a = "Senai.txt"
    with open(a,"a")as carteira:
        carteira.write(f"{carteira.nome}: {carteira.notas} R$ | {carteira.moedas} R$")

salvando = salvando(lista_carteira)"""