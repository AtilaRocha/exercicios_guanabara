#DESAFIO 011
# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS.
# CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSARIA PARA PINTÁ-LA,
# SABENDO QUE CADA LITRO DE TINTA, PINTA UMA ÁREA DE 2M².

l = float(input('Medição da Largura em metros:'))
a = float(input('Medição da Altura em metros:'))

area = l * a

total = area /2

print(f'Sua parede tem a dimensão de {l}x{a}m. '
      f'A área total a ser pintada é de: {area}m².\n'
      f'Para pintar essa parede, será necessario '
      f'{total:.2f} litros de tinta para pintura!')