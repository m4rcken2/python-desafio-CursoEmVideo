#Exercício Python 30: 
#Crie um programa que leia um número inteiro 
# E mostre na tela se ele é PAR ou ÍMPAR.

num_int = int(input('Digite um número inteiro: '))
if (num_int % 2 == 0):
    print('{} é PAR'.format(num_int))
else:
    print('{} é IMPAR'.format(num_int))
