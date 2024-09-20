"""Crie um algoritimo que leia 5 numeros inteiros e, em seguida mostre:
1- Quantidade de numeros pares
2- Quantidade de numeros impares
3- Quantidade de numeros positivos
4- Quantidade de numeros negativos
"""

import os
os.system("cls||clear")
import random

QTD = 5
list_num = []

#Verificação:

for i in range(QTD):
    num = random.randint(-10,10)
    list_num.append(num)
    
def verificação_pares_impar (a):
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
    return quantidade_pares, quantidade_impares

def verificação_nega_posi(a):
    quantidade_nega=0
    quantidade_posi=0
    for numero in a:
        if numero >= 0:
            quantidade_posi+=1
        else:
            quantidade_nega+=1
    return quantidade_posi, quantidade_nega

qtd_posi, qtd_nega = verificação_nega_posi(list_num)
''
qtd_impar, qtd_par = verificação_pares_impar(list_num)

#Imprimindo resultado:

print(f"""\033[31mPares: {qtd_par}
Impares: {qtd_impar}
Positivos: {qtd_posi}
Negativos: {qtd_nega}\n\033[m""")

for i,numero in enumerate(list_num):
    print(f"{i+1}º Numero: {numero}")
