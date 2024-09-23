 # João Victor Agapio Modesto Mendes | Bruno Henrique Alves Santos | Leonardo Machado Britto | Nicolas Roger

import os
import random
os.system ("cls || clear ")
import time

numeros_armazenados = []
QTD = 5

def logo_senai():
    print("""\033[34m
===============
---  \033[37mSENAI\033[34m  ---
===============  \033[m        

""")
    
# Solicitando dados:
logo_senai()
for i in range (QTD):
    """numeros=int(input(f"\033[1;32m{i+1}º numero: "))"""
    numeros = random.randint(-10 , 10)#Apenas para teste rapidos.
    print(f"\033[1;32m{i+1}º numero: {numeros}")
    numeros_armazenados.append(numeros)
    time.sleep(0.5)
os.system("cls||clear")

#Processando dados:

def impar_par (a):
    lista_impar= []
    lista_par =[]
    for numeros in a:
        if numeros % 2 == 0:
            lista_par.append(numeros)
        else:
            lista_impar.append(numeros)
    return lista_impar , lista_par
impares,pares = impar_par(numeros_armazenados)

def positivo_negativo(a):
    lista_negativo = []
    lista_positivo = []
    for numeros in a :
        if numeros < 0 :
            lista_negativo.append(numeros)
        else:
            lista_positivo.append(numeros)
    return lista_positivo, lista_negativo

positivo, negativo = positivo_negativo(numeros_armazenados)

def media (a):
    qtd = len(a)
    soma = sum(a)
    for numero in a:
        if  (numero>=0) or (numero <0):
            media = soma/qtd
            return media
        else:
            return 0

#Retornando dados para impressão:
media_total = media(numeros_armazenados)
media_impares=media(impares)
media_pares=media(pares)
maior = max(numeros_armazenados)
menor = min(numeros_armazenados)

#Saida de dados:
logo_senai()
time.sleep(1)
print("\n\033[4;37m======= QUANTIDADE ========\033[m\n")
print(f"\033[1;30mA quantidade de número pares foram de {len(pares)}")
print(f"A quantidade de número ímpares foram de {len(impares)}")
print(f"A quantidade de número positivos foram de {len(positivo)}")
print(f"A quantidade de número negativos foram de {len(negativo)}")
time.sleep(1)
print("\n\033[4;37m======= MAIOR E MENOR ========\033[m\n")
time.sleep(1)
print(f"\033[1;30mO maior número é: {maior}")
print(f"O menor número é: {menor}")
time.sleep(1)
print("\n\033[4;37m======= MÉDIA ========\033[m\n")
time.sleep(1)
print(f"\033[1;30mA média dos números pares foram {media_pares}")
print(f"A média dos números impares foram {media_impares:}")
print(f"A média dos números totais foram {media_total:}")

time.sleep(1)

print("\n\033[4;37m======= ORDEM REVERSA ========\033[m\n")
time.sleep(1)

for i, numeros_inseridos in enumerate (reversed(numeros_armazenados)):
   print(f"\033[1;30m{len(numeros_armazenados) - i}° numero: {numeros_inseridos}")
   time.sleep(0.1)