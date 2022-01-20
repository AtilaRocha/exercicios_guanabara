# DESAFIO 044
# Elabore um programa que calcule o valor ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão? 20% de juros


# Nome da Loja
print(f'{"Lojas Átila":=^40}')

# Perguntar o Preço
conta = float(input('Preço das compras: \nR$'))

# Indicar formas de Pagamento!
print('FORMAS DE PAGAMENTO\n'
'[1] à vista dinheiro/chegue\n'
'[2] à vista cartão\n'
'[3] 2x no cartão\n'
'[4] 3x no cartão ou mais')

# Perguntar qual a forma de pagamento
opção = int(input('Qual é a opção?\n'))

# Calculando os PAGAMENTOS
if opção == 1:
    desconto = conta * 0.10
    N_conta = conta - desconto
    print(f'Sua compra foi no valor de R${conta:.2f} e com 10% de desconto de R${desconto:.2f} tendo novo valor de R${N_conta:.2f}.')
elif opção == 2:
    desconto = conta * 0.05
    N_conta = conta - desconto
    print(f'Sua compra foi no valor de R${conta:.2f} e com 5% de desconto de R${desconto:.2f} tendo novo valor de R${N_conta:.2f}.')
elif opção == 3:
    parcelas = conta / 2
    print(f'Sua compra de R${conta:.2f} vai custar duas parcelas de {parcelas} SEM JUROS.')
elif opção == 4:
    Num_parcelas = int(input('Quantas parcelas?\n'))
    juros = conta * 0.20
    N_conta = conta + juros
    parcelas = N_conta / Num_parcelas
    print(f'Sua compra no valor de R${conta:.2f} foi parcelado em {Num_parcelas}x tendo R${juros:.2f} de juros, sendo cada parcela de R${parcelas:.2f} totalizando R${N_conta:.2f}.')
else:
    total = 0
    print(f'OPÇÃO INVALIDA DE PAGAMENTO. Tente novamente!  ')