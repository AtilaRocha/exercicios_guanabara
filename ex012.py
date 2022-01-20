# DESAFIO 012
# FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO
# E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO.

valor_original = float(input("Valor do Produto: R$"))

valor_desconto = valor_original * 0.05

valor_novo = valor_original * 0.95

print(f'O desconto para este  produto será de: R${valor_desconto:.2f} !\n'
      f'Seu novo valor é de: R${valor_novo:.2f} !')

