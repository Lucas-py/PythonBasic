'''
Iniciando funções em python
-Criando duas funções,
onde as duas serão imprimidas em uma outra função
'''
def Saudacao(ola):
    return ola # função 'Saudacao' retornando paramêntro 'Ola'

def Nomes(nome):
    return nome # Função 'Nomes' retornando paramêntro 'Nome'

def Imprimir(saudacao, nome): #  Função onde sera imprimido as duas funções anteriores
    print(f'{saudacao}. sr {nome}')

saud = Saudacao('Ola') #  Aplicando valor ao paramêntro 'Ola' da função 'Saudacao'
nom = Nomes('Lucas') #  Aplicando o valor ao pramêntro 'nome' da função 'Nomes'

Imprimir(saud,nom) #  passando os valores para  os paramentro e executando a função 'Imprimir'