# Receba o salário base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse funcionário tem
# uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de imposto sobre o salário base.


salario = float(input('\nDigite o salário do funcionário: '))

salario_liquido = (salario * 1.05) - salario * 0.07

print(f'\nO salário liquido do funcionário é de: {salario_liquido:.2f}')
