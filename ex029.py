# DESAFIO 028
# ESCREVA UM PROGRAMA QUE LEAI A VELOCIDADE DE UM CARRO. SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
# A MULTA VAI CUSTAR R$7,00 POR CADA KM ACIMA DO LIMITE.


vel = float(input('Qual é a velocidade atual do carro?\n'))

if vel>80.0:
    multa = (vel - 80)*7
    print(f'MULTADO! Você excedeu o limite permitido que é de 80Km/h\n'
          f'Você deve pagar uma multa de R${multa:.2f}!\n'
          f'Respeite o limite de velocidade.')

print(f'Tenha um bom dia. Dirija com cuidado!')