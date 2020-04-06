def soma (n1,n2):
    resultado = n1 + n2
    if resultado > 5:
        return f'{n1} + {n2} = {resultado} menor que 5'
    else:
        return f'{n1} + {n2} = {resultado} maiorr que 5'

num1 = int(input('Dgite um número: '))
num2 = int(input('Digite outro número: '))

Resultado = soma(num1,num2)
