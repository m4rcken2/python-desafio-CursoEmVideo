#Exercício Python 28:
#Escreva um programa que faça o computador “pensar” em um número inteiro 
# entre 0 e 5 e peça para o usuário tentar 
# descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

computador = randint(0,5)

print('-=-'* 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

num = int(input('Em que número eu pensei? '))
if(num == computador):
    print('PARABÉNS! você conseguiu me vencer')
else:
    print('GANHEI! eu pensei no número {} e não no {}'.format(computador, num))