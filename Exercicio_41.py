# Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês.Imprima o valor
# a ser pago ao funcionário, adicionando 10% sobre o valor calculado.


valor_hora = float(input('\nDigite o Valor da Hora de Trabalho: R$ '))
quanta_hora = float(input('Digite a Quantidade de Horas Trabalhadas: '))

pagamento = (quanta_hora * valor_hora) * 1.10

print(f'\nO salário a ser pago é de: R$ {pagamento:.2f} Reais')
