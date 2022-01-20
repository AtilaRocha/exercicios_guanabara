# DESAFIO 035
# DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRES RETAS
# E DIGA AO USUARIO SE ELAS PODEM OU NÃO FORMAR UM TRIANGULO.


print("-="*20)
print('Analisador de Triângulos')
print("-="*20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima PODEM formar um Triângulo!')
else:
    print('Os segmentos acima NÂO PODEM formar um Triângulo!')
