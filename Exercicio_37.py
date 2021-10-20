# Faça um programa que leia um valor de um produto e imprima o valor com desconto tendo em vista que o desconto é de 12%.


prod = float(input('\nDigite o valor do produto: '))

desc = prod * 0.88

print(f'\nO valor do produto com desconto é de: {desc:.2f}')
