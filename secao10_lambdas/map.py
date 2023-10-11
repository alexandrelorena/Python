"""
Map
- Mapeamento de valores para função.
"""
import math

print('\n------------- ↓ Map ↓ -------------\n')


def area(r):
    """Calcula a área de um círculo com raio 'r'"""
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

print('\n------------- ↓ forma comum: ↓ -------------\n')

areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

print('\n------------- ↓ utilizando Map: ↓ -------------\n')

areas = map(area, raios)  # recebe 2 parâmetros >> 1º - a função; 2º - um iterável

print(areas)
print(type(areas))

print(list(areas))  # convertendo pra lista

# print(tuple(areas))  # convertendo pra tupla

# print(dict(areas))  # convertendo pra dicionário

# print(set(areas))  # convertendo pra conjunto - set

print('\n------------- ↓ utilizando Map com Lambda: ↓ -------------\n')

print(list(map(lambda r: math.pi * (r ** 2),  raios)))

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28),
           ('Londres', 22)]

print(cidades)
print(type(cidades))

#  converter para Fahrenheit >> f = 9/5 * c + 32

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

# 1º forma
print(list(map(c_para_f, cidades)))

# 1º forma
print(list(map(lambda dado: (dado[0], (9/5) * dado[1] + 32), cidades)))

