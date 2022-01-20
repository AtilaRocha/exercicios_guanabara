#DESAFIO 004
# Faça um programa que leia algo pelo teclado e mostre na tela o seu
# tipo primitivo e todas as informações possiveis sobre ele.

n = input('Digite algo:')

print('Só tem numeros', n.isnumeric())
print('', n.isalnum())
print('', n.isascii())
print('', n.isprintable())