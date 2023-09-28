
"""
Módulo Collections - Named Tuple

Collections >> High-performance Container Datetypes

Named Tuple -> São tuplas diferenciadas onde especificamos um nome e parâmetros.

"""
# Ex de tupla
tupla = (1, 2, 3)
print(tupla[2])

from collections import namedtuple

# Forma 1 >> declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 >> declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 >> declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

#  Usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

print(ray)
# Acessando dados - forma 1

print(ray[0])
print(ray[1])
print(ray[2])

# Acessando dados - forma 2

print(ray.idade)
print(ray.raca)
print(ray.nome)

print(ray.index('Chow-Chow'))

print(ray.count('Chow-Chow'))
