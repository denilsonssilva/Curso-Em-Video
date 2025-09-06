pro = float(input('Qual o preço do produto? R$'))
des = pro - (pro * 0.05) 

print(f'Este produto esta em promoção, custando apenas R${des:.2f}\nDesconto de R${pro * 0.05:.2f}')