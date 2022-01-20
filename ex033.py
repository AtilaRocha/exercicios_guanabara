# DESAFIO 033
# FAÇA UM PROGRAMA QUE LEIA
# TRES NUMEROS E MOSTRE QUAL É O MAIOR E QUAL É O MENOR

a = float(input('Digite o primeiro valor:'))
b = float(input('Digite o segundo valor:'))
c = float(input('Digite o terceiro valor:'))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O Maior valor digitado é {maior}!')
print(f'O Menor valor digitado é {menor}!')
