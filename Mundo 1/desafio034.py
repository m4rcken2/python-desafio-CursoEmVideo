#Exercício Python 34: 
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o sálario do funcionário? '))

if salario <= 1250:
    aumento = (salario * 0.15) + salario
else:
    aumento = (salario * 0.1) + salario
print('Você ganhava $R{:.2f} passa a ganhar $R{:.2f} '.format(salario, aumento))
