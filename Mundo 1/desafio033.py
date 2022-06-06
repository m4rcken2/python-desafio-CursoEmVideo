#Exercício Python 33: 
#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))
min = v1
if v2<v1 and v2<v3 :
    min = v2
if v3<v2 and v3<v1:
    min = v3

max = v1
if v2>v1 and v2>v3:
    max = v2
if v3>v1 and v3>v2:
    max = v3

print('O menor valor digitado foi {}'.format(min))
print('O maior valor digitado foi {}'.format(max))