larg = float(input('Qual é a largura da parede?: '))
alt = float(input('Qualé a alture da parede ?: '))

area = larg * alt
nlitro = area / 2

print('A Área da parede é {} metros quadrados e a quantidade de tinta necessária pra pintá-la é {} litros'.format(area, nlitro))
