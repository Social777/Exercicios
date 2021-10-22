# Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual.


idade = int(input('\nDigite a sua idade: '))
ano = int(input('Digite o ano atual: '))

ano_nascimento = ano - idade

print(f'\nO ano em que você nasceu é: {ano_nascimento}')
