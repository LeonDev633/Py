"""Crie um programa que vai gerar cinco números aleatórios e 
colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique
o menor e o maior valor que estão na tupla."""

import os
os.system("cls||clear")
from random import randint

tuplas = ()
lista_numeros =[]
contador = 0

while True:
    num = randint(1,100)
    contador += 1
    lista_numeros.append(num)
    tuplas = lista_numeros
    if contador == 5:
        break
for numero in tuplas:
    print(f" Numero: {numero}", end = " " )

mai = max(tuplas)
min = min(tuplas)

print(f"\nMaior numero: {mai}")
print(f"\nMenor numero: {min}")