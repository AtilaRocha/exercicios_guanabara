# DESAFIO 022
# CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
# - O NOME COM TODAS AS LETRAS MAIÚSCULAS.
# - O NOME COM TODAS MINÚSCULAS.
# - QUANTAS LETRAS AO TODO (SEM CONSIDERAR ESPAÇOS.)

nome = str(input("Digite seu nome Completo: ")).strip()
print('Analisando seu nome...')


print(f'Seu nome em maiúsculas é: {nome.upper()}.\n '
      f'Seu nome em minúsculas é: {nome.lower()}.\n'
      f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras\n'
      f'Seu primeiro nome é {len(nome[0])} e tem {nome.find(" ")} letras.')
"""Seu primeiro nome é {nome.find(" ")} e ele tem {} letras."""
separa = nome.split()

print(separa)




