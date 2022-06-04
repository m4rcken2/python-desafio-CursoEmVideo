nome = str(input('Digite seu nome completo: '))

print('Seu nome em maiúsculas {}'.format(nome.upper()))
print('Seu nome em minusculas {}'.format(nome.lower()))

lenW = len(nome) - nome.count(" ")

print('Seu nome tem {} letras'.format(lenW))

splitn = nome.split()

print('Seu primeiro nome tem {} letras'.format(len(splitn[0])))
