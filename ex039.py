# DESAFIO 039
# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do
# prazo.


from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento:'))

idade = atual - nasc

print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')

if idade == 18:
    print(f'Precisa Alistar IMEDIATAMENTE!')
elif idade > 18:
    a = idade - 18
    D = atual - a
    if a == 1:
        print(f'Passou {a} ano para alistamento')
    else:
        print(f'passou {a} anos do alistamento')
    print(f'Seu alistamento foi em {D}')
elif idade < 18:
    a = 18 - idade
    D = a + atual
    if a == 1:
        print(f'Falta {a} ano para alistamento')
    else:
        print(f'Faltam {a} anos para alistamento')
    print(f'Seu alistamento será em {D}')