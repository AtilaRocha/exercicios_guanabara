# DESAFIO 019
# FAÇA UM PROGRAMA Q LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO
# SENO, COSSENO E TANGENTE DESSE ÂNGULO.#

import math

angulo = float(input('Digite o ângulo:'))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O ângulo de {angulo} possui o SENO de {seno:.2f}!\n'
      f'O COSSENO de {cosseno:.2f}!\n'
      f'A TANGENTE de {tangente:.2f}!')



