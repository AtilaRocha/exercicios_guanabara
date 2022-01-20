# Desafio 052
# Faça um progrtama que leia um número inteiro e diga se ele é ou não um número primo.

# Lendo um número inteiro
n = int(input('Digite um número:\n'))

tot = 0
# Indentificando se é primo ou não
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {n} foi divisível {tot} vezes.')
if tot == 2:
    print(f'O número {n}, é primo!')
else:
    print(f'O número {n}, não é primo!')