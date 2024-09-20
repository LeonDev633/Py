import os 
os.system("cls||clear")

"""Escreva um programa para aprovar o empréstimo bancário 
para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e
em quantos anos ele vai pagar. A prestação mensal não 
pode exceder 30% do salário ou então o empréstimo será negado."""

casa=int(input("Valor do imovel: "))
renda = int(input("Salário:"))
pagamento = int(input("Em quantos anos quer parcelar: ")) 

valor_mns: float =casa/(pagamento * 12)
max_salario= renda * 0.3
if valor_mns <= max_salario:
    print("Emprestimo aprovado")
    print(f"Valor: {valor_mns:.2f}")
else:
    print("Emprestimo negado")