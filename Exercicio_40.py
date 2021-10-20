# Uma empresa contrata um encanador a R$ 30.00 por dia. Faça um programa que solicite o número de dias trabalhados pelo
# encanador e imprima o a quantia líquida que deverá ser paga, sabendo que são descontados 8% para imposto de renda.


dia_trabalhado = int(input('\nDigite a quantidade de dia Trabalhados: '))

""" Se a questão quisesse mais informações tipo a quantidade bruta ou a quantidade em valor que estava sendo descontado
o código de cálculo iria ser diferente desse"""
salario_liquido = (dia_trabalhado * 30) - ((dia_trabalhado * 30) * 0.08)

print(f'\nO Salário liquido a ser pago é de: R$ {salario_liquido:.2f}')
