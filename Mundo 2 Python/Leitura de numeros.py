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

while True:
    num = random.randint(-10,10)
    list_num.append(num)
    if num == 0:
        break
    
def verificação_pares_impar (a):
    quantidade_pares = 0
    quantidade_impares = 0
    list_par=[]
    list_impar = []
    for numero in a:
        if numero %2==0:
            quantidade_pares +=1
            list_par.append(numero)
        else:
            quantidade_impares +=1
            list_impar.append(numero)
    return quantidade_pares, quantidade_impares

def verificação_nega_posi(a):
    quantidade_nega=0
    quantidade_posi=0
    qtd_posi_par = 0
    for numero in a:
        if numero > 0:
            quantidade_posi+=1
            if numero %2 ==0:
                qtd_posi_par+=1
        else:
            quantidade_nega+=1
    quantidade_nega+=-1    
    return quantidade_posi, quantidade_nega,qtd_posi_par

qtd_posi, qtd_nega,qtd_par_posi = verificação_nega_posi(list_num)
''
qtd_par, qtd_impar = verificação_pares_impar(list_num)
quantidade = len(list_num)
#Imprimindo resultado:

print(f"""\033[31mImpares: {qtd_impar}
Pares: {qtd_par}
Positivos: {qtd_posi}
Negativos: {qtd_nega}
Positivos pares: {qtd_par_posi}
Quantidade de numeros inseridos: {quantidade}
\n\033[m""")

for i,numero in enumerate(list_num):
    print(f"{i+1}º Numero: {numero}")
