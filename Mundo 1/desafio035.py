#Exercício Python 35: 
#Desenvolva um programa que leia o comprimento de três retas e
#diga ao usuário se elas podem ou não formar um triângulo.

print('+=' * 20)
print('Analisador de triangulos')
print('+=' * 20)

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if (s1 < s2 + s3) and (s2 < s1+ s3) and (s3 < s1 + s2 ):
    print('Os segmentos acima podem formar um triângulo')
else:
    print('Os segmento acima não podem formar um triângulo')