import random
import os
import time

os.system("cls||clear")


while True:
    while True:
        num=random.randint(1,10)
        derrotas = 0
        vitoria = 0
        tentativa=0
        for i in range(3):
            print("="*40)
            print(f"{"ACERTE O NUMERO":^40}")
            print("="*40)
            print(f"{"Derrotas: ":^15}{derrotas}",end=" ")
            print(f"{"Vitorias: ":^15}{vitoria}")
            print("="*40)
            print(f"{"DICA":^40}")
            print(f"{"EU PENSEI EM UM NUMERO ENTRE 1 E 10":^40}")
            print("="*40)
            
            tentativa = i+1
            numero=int(input(f"{tentativa}ª Tentativa: "))
            if numero == num:
                print("\033[2;35mVocê acertou !\033[m")
                vitoria +=1
                time.sleep(2)
                os.system("cls||clear")
                break
            elif numero != num:
                print("Você errou, tente novamente.")
                time.sleep(1)
                os.system("cls||clear")
                if  tentativa == 3:
                    derrotas+=1
                    print("="*40)
                    print(f"{"Você usou o numero maximo de tentativas":^40}")
                    print("="*40)
                    os.system("cls||clear")
                    
                    