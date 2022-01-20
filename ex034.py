# DESAFIO 034
# ESCREVA UM PROGRAMA QUE PERGUNTE O SALARIO DE UM FUNCIONARIO
# E CALCULE O VALOR DO SEU AUMENTO.
# PARA SALÁRIOS SUPERIORES A R$1.250,00 CALCULE UM AUMENTO DE 10%
# PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%.

s = float(input('Qual o ordenado do estimadíssimo Operario?\n'))

if s > 1250:
    ajuste = (s * 0.10) + s
    bonus = s * 0.10
    porc = 10
else:
    ajuste = (s * 0.15) + s
    bonus = s * 0.15
    porc = 15
print(f'Quem ganhava R${s:.2f} agora passa a ganhar R${ajuste:.2f},\n'
      f'recebendo um ajuste de {porc}%, seu bonus foi de R${bonus:.2f}!')