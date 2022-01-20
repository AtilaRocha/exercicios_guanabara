# DESAFIO 019
# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR
# O QUADRO. FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E
# ESCREVENDO O NOME DO ESCOLHIDO.

from random import choice

a1 = str(input('Digite o nome do primeiro aluno: \n'))
a2 = str(input('Digite o nome do segundo aluno: \n'))
a3 = str(input('Digite o nome do terceiro aluno: \n'))
a4 = str(input('Digite o nome do quarto aluno: \n'))

list = (a1, a2, a3, a4)

print(f'O Aluno escolhido foi {choice(list)}!')









