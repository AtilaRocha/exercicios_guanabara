# DESAFIO 023
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA
# CADA UM DOS DÍGITOS SEPARADOS.
# EX:
# Digite um Número: 1834

# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar:1

num = int(input('Informe o número desejado: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {u}!')


print(f'Unidade: {u}! \n'
      f'Dezena: {d}! \n'
      f'Centena: {c}!\n'
      f'Milhar {m}! \n')



