# Leia um valor em segundos e imprima-o em horas, minutos e segundos.


segundo = int(input('\nDigite a quantidade de segundos: '))

hora = segundo / 3600
minuto = segundo / 60

print(f'\nAgora são {hora.__int__()} horas, {minuto.__int__()} minutos e {segundo} segundos')
