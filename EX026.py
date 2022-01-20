# DESAFIO 026
# FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
# - QUANTAS VEZES APARECE A LETRA "A".
# - EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ.
# - EM QUE POSÇÃO ELA APARECE A ÚLTIMA VEZ.

frase = str(input('Digite uma frase:')).upper().strip()

print(f'A letra A aparece {frase.count("A")} vezes na frase.\n'
f'A primeira letra A apareceu na posição {frase.find("A""Á")+1}.\n'
f'A última letra A apareceu na posição {frase.rfind("A")+1}.')





