# DESAFIO 027
# FAÇA UM PROGRAMA QUE LEAI O NOME COMPLETO DE UMA PESSOA, MOSTANDO
# EM SEGUIDA O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE.
# EX: Ana Maria de Souza
# primeiro nome = Ana
# último nome = Souza

nm = str(input('Digite seu nome completo:')).strip()
n = nm.split()


print(f'Muito prazer em te conhecer!\n'
      f'Seu primeiro nome é {n[0]}\n'
      f'Seu último nome é {n[len(n)-1]}')


