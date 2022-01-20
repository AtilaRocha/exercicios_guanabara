# Desafio 051
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

# Introdução
print('='*20)
print('10 Termos de uma PA')
print('='*20)

# Pegando os termos
primeiro = int(input('Primeiro termo:'))
razão = int (input('Razão:'))
decimo = primeiro + (10 - 1) * razão

# Laços
for c in range(primeiro, decimo + razão, razão):
    print(f'{c}', end=' → ')
print('Acabou')