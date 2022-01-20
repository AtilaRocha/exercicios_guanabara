# DESAFIO 020
# O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE
# APRESENTAÇÃO DE TRABALHOS DOS ALUNOS. FAÇA UM PROGRAMA QUE LEIA O NOME
# DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA.


from random import shuffle

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

list = (a1, a2, a3, a4)

print(f'A ordem de apresentação do trabalho será:!')
print(list)