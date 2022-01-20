# Desafio 065
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usu´´ario se ele quer ou não continuar a digitar valores.

n1 = float(input("Qual o Primeiro Número? "))
n2 = float(input("Qual o Segundo Número? "))

if n1 > n2:
    print(f'O número {n1} é o maior!')
else:
    print(f'O número {n2} é o maior!')