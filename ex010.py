# DESAFIO 010
# CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA
# TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR.
# CONSIDERE: U$$ 1.00 = R$ 3.27 2017
# CONSIDERE: U$$ 1.00 = R$ 5.57 2021

carteira = float(input('Quanto você quer gastar?'))

d17 = carteira / 3.27

d21 = carteira / 5.52

print(f'Com R${carteira} seu poder de compra é:\n'
      f'Em 2017 você conseguiria comprar U$${d17:.3f}\n'
      f'Em 2021 você consegue comprar U$${d21:.3f}')















