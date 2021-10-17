# Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares.


real = float(input('\nDigite o valor em Reais: '))
cot = float(input('Digite a Cotação do Dólar: '))
dolar = real / cot

print(f'\nO valor em Dólares é de: {dolar}')
