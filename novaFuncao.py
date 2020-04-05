'''
1 - Crie uma função que exiba uma saudação com os parâmentros saudacoes e nome
'''
def saudacao(nome,saudacoes):
    print(saudacoes, nome)

name = input('insira seu nome: ')
saudacao(name, 'Olá Sr.')

'''
2 - crie uma função que receba 3 números com parâmentros e exiba asoma entre eles
'''
         #parametros
def soma(n1,n2,n3):
    cal  = n1 + n2 + n3
    print(f'{n1} + {n2} + {n3} = {cal}')

num1 = int(input('insira um numero: '))
num2 = int(input('Insira outro numero: '))
num3 = int(input('Insira mais um numero: '))

soma(num1,num2,num3)

'''
3 - Crie uma função que receba 2 números. O primeiro é um valor é o segundo e um 
percentual (ex: 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
'''

def porcentagem (n,p):

    return n + (n * p / 100 )

percentual = int(input('Insira o numero da porcentagem: '))
num = int(input('Insira um número: '))

resultado = porcentagem(num, percentual)
print(resultado)