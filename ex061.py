# Desafio 061
# Refaça o Desafio 51. Lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

# Introdução
print('='*20)
print('10 Termos de uma PA')
print('='*20)

# Coletando variaveis
term = int(input('Primeiro Termo: '))
r = int(input('Razão: '))

# Acumuladores
fim = False
num = term
num2 = -1

# Fazendo calculo
while not fim:
    if num == 8 * r + term:
        fim = True
    else:
        num2 += 1
        num = term + (num2 * r)
        print(f'{num}', end='=>')
print('FIM')