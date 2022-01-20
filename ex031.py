# DESAFIO 031
# DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTANCIA DE UMA VIAGEM EM KM.
# CALCULE O PREÇO DA PASSAGEM, COBRANDO R$0,50 POR KM PARA VIAGENS DE
# ATÉ 200KM
# E R$0,45 PARA VIAGENS MAIS LONGAS.

d = float(input('Qual a distancia em KM de sua viagem?'))

"""if d<=200:
    valor = d * 0.5
    print(f'O preço da sua passagem será de R${valor:.2f}')
else:
    valor_promo = d * 0.45
    print(f'O preço da sua passagem será de R${valor_promo:.2f}')
print(f'Você está prestes a começar uma viagem de {d}Km!')"""

print(f'Você está prestes a começar uma viagem de {d}Km!')
valor = d * 0.5 if d<=200 else d * 0.45
print(f'O preço da sua passagem será de R${valor:.2f}')
