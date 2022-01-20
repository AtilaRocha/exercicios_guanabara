# DESAFIO 040
# Cire um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5. a 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))

m = (n1 + n2) / 2
print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {m}.')
if m < 5:
    print(f'REPROVADO')
elif m <= 6.9:
    print(f'RECUPERAÇÃO')
elif m >= 7:
    print(f'APROVADO')

p = str(input('[ 1 ]'
              '[ 1 ]'
              '[ 1 ]'
              '[ 1 ]'))


