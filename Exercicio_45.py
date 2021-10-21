# Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela ASCII para resolver o problema.


letra_maiuscula = str(input('\nDigite uma letra maiúscula: '))

numero = ord(letra_maiuscula) + 32

print(f'\nA sua letra minuscula correspondente é: {chr(numero)}')
