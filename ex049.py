# Desafio 049
# refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

# Lendo Número
n = int(input('Digite o número desejado aqui:'))

# Criando laço
print(f'A tabuada de {n} é:\n')
for t in range(0, 11):
    print(f'{n} x {t} = {n*t}')




