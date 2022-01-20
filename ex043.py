# DESAFIO 043
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

a = float(input('Qual sua altura(m)?'))
p = float(input('Qual seu peso(kg)?'))

imc = p / (a ** 2)

if imc < 18.5:
    print(f'Abaixo do peso')
elif imc <= 25:
    print(f'Peso Ideal')
elif imc <= 30:
    print(f'Sobrepeso')
elif imc <= 40:
    print(f'Obesidade')
elif imc > 40:
    print(f'Obesidade Mórbida')
print(f'O IMC dessa pessoa é de {imc:.1f}!')
