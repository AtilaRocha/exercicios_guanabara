# DESAFIO 042
# Refaça o DESAFIO 035 dos triângulos, acrescentando o
# recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isóceles: dois lados iguais
# - Escaleno: todos os lados diferentes


print("-="*20)
print('Analisador de Triângulos')
print("-="*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))


if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima PODEM formar um Triângulo!', end='')
    if r1 == r2 == r3:
        print(f' Equilátero')
    elif r1 != r2 != r3 != r1:
        print(f' Escaleno')
    else:
        print(f'ISÓSCELES')
else:
    print('Os segmentos acima NÂO PODEM formar um Triângulo!')


  ## """ (f'Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
  #  (f'Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
   # (f'Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!')"""