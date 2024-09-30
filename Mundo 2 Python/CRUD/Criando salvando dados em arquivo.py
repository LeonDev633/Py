import os
from dataclasses import dataclass

os.system("cls||clear")

#Estrutura de dados:
@dataclass
class Aluno:
    nome:str
    idade:int

quantidade_de_alunos=2
lista_alunos=[]

#Solicitando dados:
for i in range(quantidade_de_alunos):
    aluno=Aluno (
        nome=input("Digite seu nome: "),
        idade=int(input("Digite sua idade: "))
    )
    lista_alunos.append(aluno)
#Mostrando alunos.
print("\n=== Exibindo dados dos alunos ===")
for aluno in lista_alunos:
    print(f"Nome: {aluno.nome}")
    print(f"idade: {aluno.idade}")

print("\n=== Salvando dados ===")

#Definindo arquivo para salvar os dados.
nome_do_arquivo = "Lista_de_alunos_SENAI.txt"

#Abrindo arquivo e definindo que será feito a escrita de cada vez.
with open(nome_do_arquivo,"w") as arquivo_alunos: #"W" apaga conteudo existente e escreve novos. "A" continua a partir do já escrito
    for aluno in lista_alunos:
        #Escrevendo no arquivo uma linha de cada vez.
        arquivo_alunos.write(f"{aluno.nome}, {aluno.idade}\n")
print("\n=== Salvos ===")




#limpando lista de alunos.
lista_alunos = []
#lendo dados de um arquivo.

print(("\n\n=== Acessando dados do arquivo ==="))
with open(nome_do_arquivo,"r") as arquivo_de_origem:#"R" para leitura do arquivo.
    for linha in arquivo_de_origem:
        nome, idade = linha.strip().split(",")
        lista_alunos.append(Aluno(nome=nome, idade=int(idade)))

for aluno in lista_alunos:
    print(f"Nome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")


#Fechamento de arquivo:
arquivo_alunos.close()
