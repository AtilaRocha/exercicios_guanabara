# Desafio 056
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

# Criando acumuladores
média_idade = 0
idade_total = 0
homem_velho = 0
nome_velho_homem = '' 
mulher_velha = 0

# Coletando dados
num_pessoas = int(input('Quantas pessoas? '))
for p in range(1, num_pessoas + 1):
    print('~~//'*5, f'{p}ª PESSOA','\\\~~'*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    # Fazendo media das idades
    idade_total += idade
    média_idade = idade_total / num_pessoas

    # Nome do mais velho
    if p == 1 and sexo in 'M':
        homem_velho = idade
        nome_velho_homem = nome
    if sexo in 'M' and idade > homem_velho:
        homem_velho = idade
        nome_velho_homem = nome

    # Descobrindo quantas mulheres tem menos de 20 anos
    if sexo in 'F' and idade < 20:
        mulher_velha += 1

# Mostrando resultados
print(f'A média de idade do grupo é de {média_idade:.2f} anos.')
print(f'O homem mais velho é {nome_velho_homem} e tem {homem_velho} anos.')
if mulher_velha == 1:
    print(f'Temos {mulher_velha} mulher abaixo dos 20.')
else:
   print(f'Temos {mulher_velha} mulheres abaixo dos 20.')