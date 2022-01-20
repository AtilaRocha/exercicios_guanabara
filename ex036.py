# DESAFIO 036
# Escreva um programa para aprovar o empréstimo bancário para a
# compra de uma casa. O programa vai perguntar o valor da casa, o salário
# do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder
# 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa: \nR$'))
salario = float(input('Quanto você ganha: \nR$'))
anos = float(input('Em quantos anos pretende pagar? \n'))

prest = casa / (anos * 12)
salario_30 = salario * 0.30

print(f'Para pagar uma casa de R${casa:.2f} em {anos:.0f} anos.\n'
      f'A prestação será de R${prest:.2f}.')

if prest > salario_30:
    print('O seu Empréstimo foi NEGADO!')
else:
    print('O seu Empréstimo foi APROVADO!')





