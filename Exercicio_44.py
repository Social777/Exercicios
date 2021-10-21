# Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada. calcule e mostre
# quantos degraus o usuário deverá subir para atingir seu objetivo.


import math
altura_degrau = float(input('\nDigite a altura do degrau da escada em centímetros: '))
altura_objetivo = float(input('Digite a altura em centímetro que o usuário quer chegar: '))

degraus = altura_objetivo / altura_degrau

print(f'\nSera necessário subir {math.ceil(degraus)} degraus para alcançar seu objetivo.')
