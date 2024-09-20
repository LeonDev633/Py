"""
Você está fazendo parte de uma equipe de desenvolvimento e precisa corrigir um código que um de 
seus colegas não concluiu. O Objetivo é criar um algoritmo que leia 5 números inteiros e, em seguida,
mostre na tela:

1. A quantidade de números pares e ímpares.
2. A quantidade de números positivos e negativos.
3. A quantidade de números inseridos.
4. O maior e o menor número.
5. A média dos números pares.
6. A média dos números ímpares.
7. A média de todos os números inseridos.
8. Mostrar os números lidos na ordem inversa.
"""

import os 
os.system("cls||clear")

import time
import random #Sorteio de numeros para teste Rapido:

QTD = 5
lista_num=[]

def logo_senai():
    print("""\033[36m
===============
---  SENAI  ---
===============  \033[m        

""")
    


# Processando dados:
    
def media (a):
    qtd = len(a)
    soma = sum(a)
    for numero in a:
        if  (numero >= 0) or (numero<=0):
            media = soma/qtd
            return media
        else:
            return 0

def processando_par_impar(a):
    quantidade_pares = 0
    quantidade_impares = 0
    list_par=[]
    list_impar = []
    for numero in a:
        if numero %2==0:
            quantidade_pares +=1
            list_par.append(numero)
        elif numero%2!=0:
            quantidade_impares +=1
            list_impar.append(numero)

    return quantidade_pares, list_par, quantidade_impares, list_impar

def processando_posi_nega (a):
    quantidade_negativo=0
    quantidade_positivo=0
    for numero in a:
        if numero >=0:
            quantidade_positivo+=1
        else:
            quantidade_negativo+=1
    return quantidade_negativo, quantidade_positivo

#Entrada de dados:

logo_senai()

print("\n=== Entrada de dados ===\n")
for i in range(QTD):
    while True:
        """numero1=random.randint(-10,10) #Teste rapido:"""
        numero1 = int(input(f"Informe o {i+1}º numero: "))
        lista_num.append(numero1)
        break

#Atribuindo valores a variaveis:

qtd_par, list_par, qtd_imp, list_impar= processando_par_impar(lista_num)
negativo, positivo = processando_posi_nega(lista_num)
md_par:float = media(list_par)
md_impar:float=media(list_impar)
md_total:float = media(lista_num)
maior_num=max(lista_num)
menor_num=min(lista_num)
qtd_total=len(lista_num)

#Imprimindo resultados:
os.system("cls||clear")
logo_senai()

print("\n=== Quantidade ===\n")
time.sleep(1)
print(f"Quantidade de pares: {qtd_par}")
print(f"Quantidade dos impares: {qtd_imp}")
print(f"Quantidade de numero negativo: {negativo}")
print(f"Quantidade de numero positivo: {positivo}")
print(f"Quantidade total de numeros inseridos: {qtd_total}")
time.sleep(1)
print(f"\n=== Médias ===\n")
time.sleep(1)
print(f"Média dos pares: {md_par}")
print(f"Média dos impares: {md_impar}")
print(f"Média de todos os numeros: {md_total}")
time.sleep(1)
print(f"\n=== Maior e menor numero ===\n")
print(f"{maior_num} é o maior numero.")
print(f"{menor_num} é o menor numero")

print("\n=== Ordem reversa dos numeros ===\n")
total= len(lista_num)
for i,numero in enumerate(reversed(lista_num)):
    print(f"{total-i}° numero: {numero}")
time.sleep(1)
print("\n====FIM====")