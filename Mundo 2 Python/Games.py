import random
import os
import time

os.system("cls||clear")

contador = 0
derrotas = 0
vitoria = 0

while True:
    num=random.randint(1,10)

    print(f"""\033[35m==== Qual numero eu pensei ? ====\033[m\n\n\033[35m ======== DICA ========\033[m\n\n O numero está entre 1 e 10.\nVocê tem 3 tentativas\n""")
    while True:
        numero=int(input("Informe o numero: "))
        if numero == num:
            print("\033[2;35mVocê acertou !\033[m")
            vitoria +=1
            os.system("cls||clear")
            time.sleep(5)
            break
        else:
            print("Você errou, tente novamente.")
            time.sleep(1)
            contador +=1
            print(f"{contador} tentativas utilizadas.")
            time.sleep(1)
            if contador == 3:
                contador = 0
                derrotas +=1
                print("Você perdeu, vamos tentar novamente com outro numero.")
                time.sleep(2)
                os.system("cls||clear")
                break
    print(f"Derrotas: {derrotas} || Vitorias: {vitoria}")
                