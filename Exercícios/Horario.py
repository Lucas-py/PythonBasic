'''
Crie um algoritmo para dar bom dia boa tarde ou boa noite
'''

horario = input('informe o horario: ')

if not horario.isdigit():
    print('digite um valor inteiro')
else:
    resultado = int(horario)

    if resultado <= 12:
        print('bom dia')
    elif resultado <= 17:
        print('boa tarde')
    elif resultado >= 18:
        print('boa noite')
    else:
        print('desculpe invalido')