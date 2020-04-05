def teste(*args):
    print(args)


#lista= [1,2,3,4,5] # lista empacotada gerando uma tupla com uma lista no indexe [0]
#teste(lista)

lista1 = [10,20,30,40,50]

lista = [0,1,2,34,5,6]

teste(* lista, lista1) # gerando uma lista desempacotada, todos os outros elementos posteiores farão parte dela e lista1 impacotada
