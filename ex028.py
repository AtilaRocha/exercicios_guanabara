# DESAFIO 028
# ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NÚMERO INTEIRO ENTRE 0 E 5 E PEÇA PARA O USUÁRIO TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO
# COMPUTADOR.
# O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU.



import random
from time import sleep
m =[0, 1, 2, 3, 4, 5]
pc = random.choice(m)
print('-='*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-='*20)

n = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(2)
if n==pc:
    print(f'PARABENS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {pc} e não no {n}!')












