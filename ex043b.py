# DESAFIO 043
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

from time import sleep

# Dados do usuário
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
sexo = str(input('Qual o seu sexo? ')).upper()

# Calcular IMC
imc = peso / (altura * altura)

# Calcular peso ideal
pi = altura * 100
pi_homem = (pi - 100) * 0.90
pi_mulher = (pi - 100) * 0.85

print('Processando os dados...')
sleep(2)

print()
print('=*='*50)
print()

if imc < 18.5:
    print(
        f' Seu IMC é {imc:.2f}\n',
        f'De acordo com seu IMC, você está abaixo do peso!'
    )
elif imc >= 18.5 and imc < 25:
    print(
        f' Seu IMC é {imc:.2f}\n',
        f'De acordo com seu IMC, você está com peso ideal!'
    )
elif imc >= 25 and imc < 30:
    print(
        f' Seu IMC é {imc:.2f}\n',
        f'De acordo com seu IMC, você está com Sobrepeso!'
    )
elif imc >= 30 and imc < 40:
    print(
        f' Seu IMC é {imc:.2f}\n',
        f'De acordo com seu IMC, você está Obeso!'
    )
else:
    print(
        f' Seu IMC é {imc:.2f}\n',
        f'De acordo com seu IMC, você esta com obesidade mórbida!'
    )
print()
print('=*='*50)
print()

if sexo == 'MASCULINO':
    print(f'Você é do sexo masculino, seu peso ideal é {pi_homem} Kg ')
else:
    print(f'Você é do sexo feminino, seu peso ideal é {pi_mulher} Kg')