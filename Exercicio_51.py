# Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua distância na origem (0,0).


x = float(input('\nDigite o x em R²: '))
y = float(input('Digite o y em R²: '))

distancia = int((((0 - x) ** 2) + ((0 - y) ** 2)) ** (1/2))

print(f'\nA distância na origem (0,0) é: {distancia}')
