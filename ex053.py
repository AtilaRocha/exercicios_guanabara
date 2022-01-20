# Desafio 053
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#Ex: Após a Sopa
#    A sacada da casa
#    A torre da derrota
#    O lobo ama o bolo
#    Anotaram a data da Maratona

# Tratando String
txt = str(input('Digite uma frase:')).strip().upper()
split = txt.split()
join = ''.join(split)
inverso = ''

# Comparando em laço
for letra in range(len(join) - 1, -1, -1):
    inverso += join[letra]
print(f'O inverso de {join} é {inverso}!')

if inverso == join:
    print(f'É um palindromo!')
else:
    print(f'Não é um palindromo!')