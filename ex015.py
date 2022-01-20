# DESEFIO 015
# ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS
# POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO.
# CALCULE O PREÇO A PAGAR. SABENDO QUE O CARRO CUSTA R$60 POR DIA E
# R$0.15 POR KM RODADO.

km = float(input('Quantos KM foram rodados?'))
dias = float(input('Por quantos dias?'))

valor_dia = dias * 60
valor_km = km * 0.15

total = valor_dia + valor_km

print(f'Por dia foi gasto R${valor_dia:.2f} e '
      f'por km rodado R${valor_km:.2f} '
      f'totalizando R${total:.2f}!')







