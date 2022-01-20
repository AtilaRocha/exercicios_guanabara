# DESAFIO 017
# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO
# ADJACENTE DE UM TRIÂNGULO RETÂNGULO. CALCULE E MOSTRE O COMPRIMENTO
# DA HIPOTENUSA.

"""from math import sqrt
c_oposto = float(input('Digite o comprimento do Cateto Oposto: '))
c_adjacente = float(input('Digite o comprimento do Cateto Adjacente: '))

hipotenusa = (c_oposto ** 2) + (c_adjacente ** 2)"""

from math import hypot

co = float(input('Digite o comprimento do Cateto Oposto: '))
ca = float(input('Digite o comprimento do Cateto Adjacente: '))

hi = hypot(co, ca)

print(f'O resultado do comprimendo da Hipotenusa é {hi:.2f}')

