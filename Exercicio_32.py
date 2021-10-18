# Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.


num = int(input('\nDigite um número inteiro: '))

print(f'\nA soma é: {(((num + 1) * 3) + ((num - 1) * 2))}')
