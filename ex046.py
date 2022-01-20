# DESAFIO 046
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 
# segundo entre elas.

# Importando Biblioteca
from time import sleep

# Iniciar Contagem

for c in range(10, -1, -1):
    print(c)
    sleep(0.5)
print('Kabum!')