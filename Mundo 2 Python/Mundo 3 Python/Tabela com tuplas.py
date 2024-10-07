import os 
os.system("cls||clear")

listagem=("Arroz", 4.90, "Macarrão", 3.90,
          "Farinha", 10.90, "Sabonete", 1.90,
          "Feijão", 7.90, "Leite", 7.90)
print("="*40)
print(f"{"PREÇOS":^40}")#Centralizando texto
print("="*40)

for item in range(0,len(listagem)):
    if item %2==0:
        print(f"{listagem[item]:.<30}", end="") #Formatação para tabelas
    else:
        print(f"R${listagem[item]:>8.2f}") #Formatação para tabelas 
print("="*40)