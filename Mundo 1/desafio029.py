#Exercício Python 29: 
#Escreva um programa que leia a velocidade de um carro. 
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
#A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Qual é a velocidade atual do seu carro? '))

if (vel > 80):
    multa = (vel - 80) * 7
    print( 'Você ultrapassou o limite permetido que é de 80km/h')
    print('Você deve pagar uma multa de $R{:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança')