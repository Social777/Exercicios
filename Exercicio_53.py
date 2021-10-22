# Faça um programa para ler as dimensões de um terreno (comprimento c e largura l), bem como o preço do metro de tela p.
# Imprima o custo para cercar este terreno com tela.

comprimento = float(input('\nDigite o comprimento do terreno: '))
largura = float(input('Digite a largura do terreno: '))
preco = float(input('Digite o preço da tela: R$ '))

custo = (comprimento * largura) * preco

print(f'\nO custo para cercar seu terreno será de R$ {custo:.2f}')
