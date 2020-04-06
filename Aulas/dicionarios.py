import  copy
'''

 Dicionários - e uma estrutura de dados que suporta um par de chave e valor
ao ser criado precisa de uma chave e um valor

'''

# d1 = {
#     # Chaves     valor
#       'chave1':'valor da chave',
#       'str': ['a','b'],
#       10 : 'outro valor',
#
# }

#v = d1.copy() #  estamos copiando parcilmente o dicionário
# v = copy.deepcopy(d1)  # realizando uma copia total do dicionário d1 através da biblioteca copy
# v[10] = 'luiz'
# v['str'][0] = 'c'
#
# print(d1)
# print(v)


# d1['nova chave'] = 'valor da nova chave' # adicionando em um dicionário

#print(d1)

# d1.update({'nome': 'lucas'}) # adicionando uma nova chave

#if d1.get('Ola') is not None:  # verificando se o valor e None
#    print(d1.get('nome da chave'))

#del d1[10]  # apagando uma chave do dicionário

#print(d1)
#print('valor' in d1.values())  # verificando se um valor existi dentro de d1

# for k in d1:
#     print(d1)

#for k in d1.items(): #  imprimindo d1 com items
#    print(k)

# for v, k in d1.items():  #  imprimindo tanto as chaves em v e  os valores em k
#     print(v, k)

clientes = {
    'cliente1': {
        'nome': 'lucas',
        'sobrenome': 'torres',
    },
        'cliente2': {
        'nome': 'piltro',
        'sobrenome': 'bala',
    },

}

for cliente_k, cliente_v in clientes.items():
    print(f'Exibindo {cliente_k}')
    for dados_k, dados_v in cliente_v.items():
        print(f'\t {dados_k} : {dados_v}')