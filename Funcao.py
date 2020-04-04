'''
Iniciando funções em python

'''
def Saudacao(ola):
    return ola

def Nomes(nome):
    return nome

def Imprimir(saudacao, nome):
    print(f'{saudacao}. sr {nome}')

saud = Saudacao('Ola')
nom = Nomes('Lucas')

Imprimir(saud,nom)