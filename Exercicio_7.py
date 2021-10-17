# Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.


fah = float(input('\nQual a temperatura em graus Fahrenheit? '))
cel = 5.0*(fah - 32.0)/9.0
print(f'\nA temperatura em Celsius é: {cel}')