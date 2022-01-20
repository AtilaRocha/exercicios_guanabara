# Desafio 054
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

# Imporanto ano atual
from datetime import date
atual = date.today().year

# Criando acumuladores
total_maior = 0
total_menor = 0

# Coletando anos
for year in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {year}ª pessoa:'))
    idade = atual - ano
    
    if idade >= 18:
        total_maior += 1
    else:
        total_menor += 1
print(f'O número de pessoas maiores de idade são {total_maior}.\n'
f'O número de pessoas menores de idade são {total_menor}.')