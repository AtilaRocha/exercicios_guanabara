# DESAFIO 045
# Crie um programa que faça o computador jogar Jokenpô


from random import randint
from time import sleep

# Criando Itens
itens = ('Pedra', 'Papel', 'Tesoura')

# Jogada aleatoria do computador
computador = randint(0, 2)

# Jogador
print(' Suas Opções:\n'
'[ 0 ] PEDRA\n'
'[ 1 ] PAPEL\n'
'[ 2 ] TESOURA\n')
jogador = int(input('Qual é a sua jogada?\n'))

# JO! KEN! PO!
print('JO!')
sleep(1)
print('KEN!')
sleep(1)
print('PO!!!')
sleep(1)

# Jogadas
print('-='*20)
print(f'O Jogador escolheu {itens[jogador]}!')
print(f'O Computador escolheu {itens[computador]}!')
print('-='*20)

# Condições
if computador == 0:
    if jogador == 0:
        print(f'ENPATE!')
    elif jogador == 1:
        print(f'JOGADOR GANHOU!')
    elif jogador == 2:
        print(f'COMPUTADOR GANHOU!')
    else:
        print(f' JOGADA INVÁLIDA!')
if computador == 1:
    if jogador == 0:
        print(f'COMPUTADOR GANHOU!')
    elif jogador == 1:
        print(f'ENPATE!')
    elif jogador == 2:
        print(f'JOGADOR GANHOU!')
    else:
        print(f'JOGADA INVÁLIDA!')   
if computador == 2:
    if jogador == 0:
        print(f'JOGADOR GANHOU!')
    elif jogador == 1:
        print(f'COMPUTADOR GANHOU!')
    elif jogador == 2:
        print(f'ENPATE!')
    else:
        print(f' JOGADA INVÁLIDA')
