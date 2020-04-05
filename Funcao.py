'''

1 - Executar o escopo de uma função dentro de outra função

'''

def Ola(saudacao):
     return f'{saudacao}'

def Imprimir(arg):
 print(arg)


saudacao = Ola('Olá')

Imprimir(saudacao)

'''

2 - Executar duas funções dentro de uma função master

'''

def nome(nome): # função nome esta retonando o nome
    return nome

def soma(n1,n2): # função soma esta retornando o resultado de n1 + n2
      return n1 + n2

def resultado(nome, soma):

     print(f'{nome} resultado {soma}')

soma1 = soma(2,2)
nome1 = nome('Lucas')

resultado(nome1.replace('L','0').upper(), soma1)