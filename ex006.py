#DESAFIO 006
# CRIE UM ALGORITMO QUE LEIA UM NÚMERO E
# MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA.

n = int(input('Digite um número:'))

d = n * 2
t = n * 3
r = n ** 0.5

print(f'O dobro de {n} é {d}, seu triplo é {t}'
      f' e sua raiz quadrada é {r:.3f}!')

#.3f até 3 casas decimais exibindo

