# DESAFIO 041
# A Confederação Nacional de Natação precisa de um programa que leia o
# idade de nascimento de um atleta e mostre sua categoria, de acordo com
# a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

from datetime import date
atual= date.today().year
nasc = float(input('Ano de Nascimento:'))

idade = atual - nasc

print(f'O atleta tem {idade:.2f} anos.')

if idade <= 9:
    print(f'Classificação: MIRIM')
elif idade <= 14:
    print(f'Classificação: INFANTIL')
elif idade <= 19:
    print(f'Classificação: JUNIOR')
elif idade <= 20:
    print(f'Classificação: SÊNIOR')
elif idade > 20:
    print(f'Classificação: MASTER')


