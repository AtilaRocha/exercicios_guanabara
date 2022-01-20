# DESAFIO 030
# CRIE UM PROGRAMA QUE LEAI UM NÚMERO INTEIRO E MOSTRE NA TELA
# SE ELE É PAR OU IMPAR.

n = int(input('Digite um número:'))
r = n % 2

if r>0:
    print(f'O número {n} é Impar')
else:
    print(f'O numero {n} é par')


