# Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa através da equação. imprima o
# resultado dessa operação.


a = float(input('\nDigite o valor de a: '))
b = float(input('Digite o valor de b: '))

hipo = ((a ** 2) + (b ** 2)) ** (1/2)

print(f'\nO valor da Hipotenusa é: {hipo}')
