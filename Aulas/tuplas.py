'''

Tuplas, não pode ser alterado nem editado, nem adiciona, nem remove e nem mudar o valor do index da tupla

'''

t = (1,2,3,4, 'a', 'b')
t1 = 1,  # tupla com um argumento

t2 = t + t1  # congatenado tuplas
print(t2)

t = list(t)  # transformando uma tupla em uma lista

t[1] = 4  # aletrando o valor do index 1

print(t)