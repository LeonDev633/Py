""" Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""

import os
os.system("cls||clear")

contador = 0 
lista=[]
tupla =()

while True:
    num = int(input("Digite um numero: "))
    lista.append(num)
    contador += 1
    if contador == 4:
        break
tupla = (lista) 
vezes=tupla.count(1)
print(tupla)
print(f"Apareceu {vezes}")
