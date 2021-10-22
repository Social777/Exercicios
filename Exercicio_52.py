# Três amigos jogam na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada um deu
# para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima
# quanto cada um ganharia do prêmio com base no valor investido.


apostador1 = float(input('\nDigite o valor apostado: '))
apostador2 = float(input('Digite o valor apostado: '))
apostador3 = float(input('Digite o valor apostado: '))
premio = float(input('\nDigite o valor do prêmio: '))

soma_aposta = apostador1 + apostador2 + apostador3

porcentagem1 = (apostador1 *100) / soma_aposta
porcentagem2 = (apostador2 *100) / soma_aposta
porcentagem3 = (apostador3 *100) / soma_aposta

premio1 = premio * porcentagem1 /100
premio2 = premio * porcentagem2 /100
premio3 = premio * porcentagem3 /100

print(f'\nO valor da contribuição do Primeiro apostador foi de: {porcentagem1:.2f}% e recebera: {premio1:.2f}')
print(f'O valor da contribuição do Primeiro apostador foi de: {porcentagem2:.2f}% e recebera: {premio2:.2f}')
print(f'O valor da contribuição do Primeiro apostador foi de: {porcentagem3:.2f}% e recebera: {premio3:.2f}')

print(f'\n*** O valores acima são aproximados ***')int()
