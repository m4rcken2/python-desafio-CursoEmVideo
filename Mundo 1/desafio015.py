dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))

total = (60 * dia) + (km * 0.15)

print('O total a pagar é de $R{:.2f}'.format(total))
