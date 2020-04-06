'''

lambda - expresão anônima, sem a necessidade de return pois ja retorna um valor.

'''

a = lambda x, y: x * y #  função anônima
print(a(5,2))

lista = [
#  P = Produto, PREÇO
          ['P1', 13],
          ['P2', 2],
          ['P3', 25],
          ['P4', 6],
          ['P5', 53]
]

lista.sort(key= lambda item: item[1])  # oranizando a lista pelo menor preço.
print(lista)
