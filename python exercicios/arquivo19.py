nome = str(input('Digite seu nome: ')).strip()
print('Seu nome em maiúscolo é: {}'.format(nome.upper()))
print('Seu nome em minúsculo é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} de letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(nome.split()[0] , len(nome.split()[0])))

