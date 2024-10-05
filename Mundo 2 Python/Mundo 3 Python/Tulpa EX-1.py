import os 
os.system("cls||clear")


numeros = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quartorze", "Quinze")
while True:
    opcao=int(input("Digite um numero de 1 a 15: "))
    if (opcao>=0) and (opcao<=15):
        break
print(f"{numeros[opcao]}")



                
                    
                    