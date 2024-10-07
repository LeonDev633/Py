from random import randint
import os
import time

os.system("cls||clear")

derrotas = 0
vitoria = 0
while True:
    print("=-"*20)
    print(f"{"ACERTE O NUMERO":^40}")
    print("=-"*20)
    print("="*40)
    print(f"{"DICA":^40}")
    print(f"{"EU PENSEI EM UM NUMERO ENTRE 1 E 10":^40}")
    print("="*40)
    tentativas = 0
    python = randint(1,10)
    for i in range (3):
        tentativas += 1
        print("="*40)
        print(f"{f"VOCÊ TEM {(i-3)*-1} TENTATIVAS RESTANTES":^40}")
        print("="*40)
        num = int(input("Qual numero eu pensei ? "))
        if num == python:
            print("*"*40)
            print(f"{f"VOCÊ ACERTOU, PARABÉNS!":^40}")
            vitoria += 1
            print("*"*40)
            time.sleep(1)
            break
        elif tentativas == 3:
            derrotas += 1
            print(f"{"VOCÊ NÃO CONSEGUIU ACERTAR":^40}")
            print(f"{f"O NUMERO QUE EU PENSEI FOI {python}":^40}")
            time.sleep(1)
            break
    os.system("cls||clear")
    print("=-"*20)
    print(f"{"Derrotas: ":^15}{derrotas}",end=" ")
    print(f"{"Vitorias: ":^15}{vitoria}")
    print("="*40)
    time.sleep(2)
        
        
        
    
 
        
                    