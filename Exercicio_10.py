# Leia uma velocidade km/h(quilômetros por hora) e apresente-a convertida em m/s (metros por segundo).


km = int(input('\nQual é a sua velocidade em km/h? '))
ms = km / 3.6
print(f'\nA velocidade em m/s(metros por segundo) é: {ms.__int__()}')