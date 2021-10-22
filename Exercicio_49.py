# Faça um programa que leia o horário (hora, minuto e segundo) de início e a duração, em segundos de uma experiência
# biológica. O programa deve resultar com o novo horário (hora, minuto e segundo) do termino da mesma.

from datetime import datetime
from datetime import timedelta

inicio = input('\nInforme o horário de início do experimento, no formado HH:MM:SS: ')

inicio = datetime.strptime(inicio, '%H:%M:%S')

segundos = int(input('Informe a duração do experimento em segundos: '))

hora_final = inicio + timedelta(seconds=segundos)
print(f'\nA hora final do experimento foi: {hora_final.time()}')

# Uma segunda forma de se fazer é:


inicio = input('\nInforme o horário de início do experimento, no formado HH:MM:SS: ')
inicio = datetime.strptime(inicio, '%H:%M:%S')
termino = input('Informe o horário de término do experimento, no formado HH:MM:SS: ')
termino = datetime.strptime(termino, '%H:%M:%S')

hora_final = termino - inicio


print(f'\nO Tempo total da experiência foi de: {hora_final} horas')
