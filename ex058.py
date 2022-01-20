# Desafio 058
# Melhore o jogo do Desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# Importando Bibliotecas
from random import randint
from time import sleep

# Criando acumulador
derrotas = 0

# Criando jogadas
print('-='*20)
print('Vou pensar em um número entre 1 e 10. Tente advinhar...')
print('-='*20)
pc = randint(0, 10)
n = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
# sleep(2)

# Repetindo jogada e dando dica.
while n != pc:
    print(f'GANHEI! Eu não pensei no número {n}!')
    if n < pc: 
        derrotas += 1       
        print(f'Maior... Tente mais uma vez.')
    elif n > pc:
        derrotas += 1
        print(f'Menor... Tente mais uma vez.')
    n = int(input('Em que número eu pensei? '))
print(f'PARABENS! Você conseguiu me vencer em {derrotas} tentativas!')