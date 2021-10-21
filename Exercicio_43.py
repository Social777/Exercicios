# Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
# -> O total a pagar com desconto de 10%;
# -> O valor de cada parcela, no parcelamento de 3x sem juros;
# -> A Comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto);
# -> A comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total);


valor_da_compra = float(input('\nDigite o valor da compra: R$ '))

compra_a_vista = valor_da_compra - (valor_da_compra * 0.10)
compra_parcelada = valor_da_compra / 3
comissao_a_vista = compra_a_vista * 0.05
comissao_parcelada = valor_da_compra * 0.05

print(f'\nO valor a vista é de: R$ {compra_a_vista:.2f} Reais')
print(f'O valor total da compra é de: R$ {valor_da_compra} Reais, e o valor da parcela é de: R$ {compra_parcelada:.2f} '
      f'Reais em 3x.')
print(f'O valor da comissão da compra a vista é de: R$ {comissao_a_vista:.2f} Reais')
print(f'O valor da comissão da compra parcelada é de: R$ {comissao_parcelada:.2f} Reais')
