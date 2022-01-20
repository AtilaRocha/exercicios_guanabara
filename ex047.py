# Desafio 047
# Crie um programa que mostre na tela todos os numeros pares que estão no intervalo entre 1 e 50.

# Importando Biblioteca
from time import sleep

# Contando números pares
for n in range(2, 52, 2):
    print(n, end=' ')
    sleep(0.5)
print('Acabou')    

