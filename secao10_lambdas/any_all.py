"""
Any e All

all() >> retorna True se todos os elementos do iterável são verdadeiros ou o iterável for vazio;

any() >> retorna True se qualquer elemento do iterável for verdadeiro. Se estiver vazio, retorna False.
"""
print('\n------------- ↓ Ex de All ↓ -------------\n')

print(all([0, 1, 2, 3, 4]))  # todos os números são verdadeiros? False

print('\n--------------------------\n')

print(all([1, 2, 3, 4]))  # todos os números são verdadeiros? True

print('\n--------------------------\n')

print(all([]))  # iterável está vazio >> True

print('\n--------------------------\n')

print(all((1, 2, 3, 4)))  # Tupla

print('\n--------------------------\n')

print(all({1, 2, 3, 4}))  # Set

print('\n--------------------------\n')

print(all('Geek'))  # String

print('\n--------------------------\n')

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristiano']

print(f'Todos os nomes têm a letra C? {all(nome[0] == "C" for nome in [nomes])}')

print('\n--------------------------\n')

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristiano', 'Daniel']

print(f'Todos os nomes têm a letra C? {all(nome[0] == "C" for nome in nomes)}')

print('\n--------------------------\n')

print(all([letra for letra in 'eio' if letra in 'aeiou']))

print('\n--------------------------\n')

print(all([letra for letra in 'eio' if letra in 'fkp'])," >>> res = [letra for letra in 'eio' if letra in 'fkp'] "
                                                        ">>> res >>> [] >> resultado é True pq o all() considera lista "
                                                        "vazia como verdadeiro!")
"""
>>> res = [letra for letra in 'eio' if letra in 'fkp'] >>> res >>> []
# resultado é True pq o all() considera lista vazia como verdadeiro
"""
print('\n--------------------------\n')

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))

print('\n--------------------------\n')

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 1]))
"""
>>> res = [num for num in [4, 2, 10, 6, 8] if num % 2 == 1]
>>> res
[]
# resultado é True pq o all() considera lista vazia como verdadeiro
"""
print('\n------------- ↓ Ex de Any ↓ -------------\n')

print(any([0, 1, 2, 3, 4]))  # True

print(any([0, False, {}, (), []]))  # False

print('\n--------------------------\n')

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Daniel']

print(any(nome[0] == 'C' for nome in nomes))

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))

