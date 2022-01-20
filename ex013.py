# DESAFIO 013
# FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO
# E MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO.

salario = float(input("Salário do Funcionário: R$"))

aumento = salario * 0.15

salario_aumento = salario * 1.15
#novo = salario + (salario * 15 / 100)


print(f"O Funcionario terá aumento de R${aumento:.2f} "
      f"totalizando {salario_aumento:.2f} !")



