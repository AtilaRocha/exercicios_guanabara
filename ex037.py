# DESAFIO 037
# Escreva um programa que leia um número inteiro qualquer e peça para o
# usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

from time import sleep
n = int(input('Digite um número inteiro:'))
print('Escolha uma das bases para conversão:')
print(f'[1] Converter para BINÁRIO\n'
      '[2] Converter para OCTAL\n'
      '[3] Converter para HEXADECIMAL\n')
opção = int(input('Sua opção:'))

print('PROCESSANDO...')
sleep(1.7)

if opção == 1:
    print(f'Convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif opção == 2:
    print(f'Convertido para OCTAL é igual a {oct(n)[2:]}')
elif opção == 3:
    print(f'Convertido para HEXADECIMAL é igual a {hex(n)[2:]}')
else:
    print('Opção inválida. Tente novamente.')

