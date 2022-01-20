# Desafio 059
# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] SOMAR
# [ 2 ] MULTIPLICAR
# [ 3 ] MAIOR
# [ 4 ] NOVOS NÚMEROS
# [ 5 ] SAIR DO programa

# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

# Lendo valores
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

# Criando acumulador
opção = 0
resposta = 0
maior = 0

# Dando opções:
print('=-'*15)
print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO programa''')
print('=-'*15)
opção = int(input('>>>>> Qual é sua opção? '))

# Fazendo os Calculos:
while opção != 5:
    if opção == 1:
        resposta = n1 + n2
        print(f'A soma entre {n1} e {n2} é {resposta}!')   
    elif opção == 2:
        resposta = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {resposta}!')
    elif opção == 3:
        maior = n1
        if n2 > n1:
            maior = n2   
        print(f'Entre {n1} e {n2} o maior número é {maior}!')
    elif opção == 4:
        print('Informe os valores novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))  
    else:
        print('Opção invalida. Tente novamente!')
    sleep(1)
    print('=-'*15)
    opção = int(input('>>>>> Qual é sua opção? '))
print('=-'*15)
print('Finalizando programa!')

