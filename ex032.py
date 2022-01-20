# DESAFIO 032
# FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO.

from datetime import date

ano = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
print(f'O ano {ano} é Bissexto!') if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 \
    else print(f'O ano {ano} não é Bissexto!')


