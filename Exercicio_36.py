# Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.


alt = float(input('\nDigite a Altura do Cilindro: '))
raio = float(input('Digite o Raio do Cilindro: '))

vol = 3.141592 * ((raio ** 2) * alt)

print(f'\nO Volume do Cilindro é de: {vol}')
