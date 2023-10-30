"""
Entendendo Iterators e Iterables

Iterator ->
    - Um objeto que pode ser iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada.

Iterable ->
    - Um objeto que irá retornar um iterator quando a função iter() for chamada.

"""
# Iterables
nome = 'Geek'
numeros = [1, 2, 3, 4, 5, 6]


it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
# print(next(it1))  # se tentar iterar na string mais vezes que o numero de caracteres, dá erro StopIteration.

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

# por baixo dos panos

for letra in nome:
    print(f'{letra}')

