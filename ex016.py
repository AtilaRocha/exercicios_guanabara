# DESAFIO 016
# CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO TECLADO
# E MOSTRE NA TELA A SUA PORÇÃO INTEIRA.
# EX: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

'''from math import trunc
n = float(input('Digite um valor:'))

print(f'O valor digitado foi {n} e a '
      f'sua porção inteira é {trunc(n)}!')'''

n = float(input('Digite um valor:'))

print(f'O valor digitado foi {n} e a '
      f'sua porção inteira é {int(n)}!')

