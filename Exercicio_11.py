# Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h(quilômetros por hora).


ms = int(input('\nQual é a sua velocidade em m/s? '))
km = ms * 3.6
print(f'\nA velocidade em km/h(quilômetros por hora) é: {km.__int__()}')