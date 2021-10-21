# Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999). Gere outro número formado pelos
# dígitos invertidos do número lido.


numero = str(input('\nDigite um número de 100 a 999: '))

print(f'\nO inverso do número digitado é: {numero[::-1]}')
