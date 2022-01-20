# Desafio 060
# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 120

# Coletando número
import numpy
num_fat = int(input('Digite o número para fatoração:'))
nums = list()
print(f'Calculando fatoração do número {num_fat}:')
for n in range(num_fat, 1, -1):
    print(f'{n}', end=' x ')
    nums.append(n)
print('1 = ', end='')
print(f'{numpy.prod(nums)}')







