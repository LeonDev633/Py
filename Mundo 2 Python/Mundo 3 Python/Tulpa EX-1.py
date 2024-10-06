"""Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de 
zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

import os 
os.system("cls||clear")


numeros = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quartorze", "Quinze")
while True:
    while True:
        opcao=int(input("Digite um numero de 1 a 15: "))
        if (opcao>=0) and (opcao<=15):
            break
    print(f"{numeros[opcao]}")
    opcao1=int(input("\nGostaria de continuar ? \n1-SIM \n2-Não"))
    if opcao1==2:
        break
    



                
                    
                    