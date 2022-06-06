#Exercício Python 27: 
# Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite seu nome completo: ').strip()
nome = nome.split()
print('Seu primeiro nome: {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[-1]))