# Desafio 048
# Faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que se encontram no intervalo de 1 até 500.


# Criando acumuladores
s = 0
cont = 0

# Range
for n in range(1, 501, 2):
    if n % 3 == 0:
        print(n, end=' ')
        s += n
        cont = cont + 1
print(f'\nO Somatório é de {s} dos {cont} números.')        