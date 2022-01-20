# Desafio 062
# Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

# Introdução
print('='*20)
print('Calculando a PA de um número')
print('='*20)

# Coletando variaveis e Acumuladores
termo = int(input('Informe o Primeiro Termo da PA: '))
r = int(input('Informe a razão da PA: '))
opção = 1
contagem = 0
n = 10

# Calculando os termos da PA
while opção != 0:
    while contagem <= n:
        print(f'{termo}', end=' => ')
        termo += r
        contagem += 1
    print('PAUSA')
    opção = int(input('\nQuantos termos a mais devem ser contados? '))
    n += opção
print(f'A progressão foi finalizada com {contagem} termos')
print('FIM!')




















