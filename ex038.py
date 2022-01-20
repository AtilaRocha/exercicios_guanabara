# DESAFIO 038
# Escreva um programa que leia dois números inteiros e compare-os,
# mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

n1 = float(input('Primeiro número:'))
n2 = float(input('Segundo número:'))

if n1 > n2:
    print(f'O Primeiro valor é maior!')
elif n1 < n2:
    print(f'O Segundo valor é maior!')
else:
    print(f'Ambos os valores são iguais.')


