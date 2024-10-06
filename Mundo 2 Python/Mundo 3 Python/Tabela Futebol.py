"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Vitoria.
"""
times=("Vitoria", "Bahia", "Corinthians", "Fluminense", "Cruzeiro",
       "Atletico - Mg", "Atletico - PR", "Internacional", "Gremio",
       "São Paulo", "Juventude", "Bragantino", "Cuiaba", "Atletico - GO", "Flamengo",
       "Fortaleza", "Criciuma", "Vasco", "Palmeiras", "Botafogo")

print("\n=== TABELA ===\n")
for i,time in enumerate(times):
    print(f"{i+1}º {time}")
print("\n=== CINCO PRIMEIROS ===\n")
for i in range (0,5):
    print(f"{i+1}º {times[i]}")
print("\n=== Zona de rebaixamento ===\n")
for i in range (16,20):
    print(f"{i+1}º {times[i]}")
print("\n=== EM ORDEM ===\n")
for i,t in enumerate(sorted(times)):
    print(f"{i+1}º {t}")

print("\n=== Posição vit ===\n")
print(f"O Vitoria está na posição {times.index("Vitoria")+1}")