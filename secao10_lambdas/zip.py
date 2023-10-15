"""
Zip

zip() -> Cria um iterável (Zip object) que agrega elemento de cada um dos iteráveis passados como entrada em pares.
"""
# ------------------------------ ↓ zip() ↓ ----------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ zip() ↓'.center(70)}\033[33m\n{'-' * 70}\033[0m\n")

# ---------------- ↓ lista, tupla, conjunto, dicionário ↓ -------------

print(f'\033[37m--------------- ↓ \033[34mlista, tupla, conjunto, dicionário \033[37m↓ ------------'
      f'---\n\033[0m')

lista1 = [1, 2, 3]
lista2 = [4, 5, 6, 12]

zip1 = zip(lista1, lista2, 'abc')

print(f'\033[31m{zip1}', end=' => ')
print(f'\033[33m{type(zip1)}\n')

zip1 = zip(lista1, lista2, 'abc')
print(f'\033[36mlista => {list(zip1)}')

zip1 = zip(lista1, lista2, 'abc')
print(f'\033[35mtupla => {tuple(zip1)}')

zip1 = zip(lista1, lista2, 'abc')
print(f'\033[34mconjunto => {set(zip1)}')

zip1 = zip(lista1, lista2)
print(f'\033[32mdicionário => {dict(zip1)}\n\033[0m')

#  o zip() utiiza como parâmetro o menor tamanho em iterável.
lista3 = [7, 8, 9, 10, 11]  # este iterável contém 2 itens a mais
zip1 = zip(lista1, lista2, lista3)
print(f'\033[31mlista com tamanhos diferentes => \033[96m{list(zip1)}')

# ---------------- ↓ usando diferentes iteráveis com zip() ↓ -------------

print(f'\n\033[37m------------ ↓ \033[34musando diferentes iteráveis com zip() \033[37m↓ ------------'
      f'---\n\033[0m')

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())

print("\033[32mtupla = 1, 2, 3, 4, 5 \n\033[36mlista = [6, 7, 8, 9, 10] \n\033[33mdicionario = {'a': 11, 'b': 12, "
      "'c': 13, 'd': 14, 'e': 15}\033[0m\n")

print(f'\033[31musando o zip() => \033[30m{list(zt)}\033[0m\n')

# ---------------- ↓ lista de tuplas com desempacotamento ↓ -------------

print(f'\n\033[37m------------ ↓\033[34mlista de tuplas com desempacotamento \033[37m↓ --------------'
      f'---\n\033[0m')
print("\033[37mdados = [(0,1), (1, 2), (2, 3), (3,4), (4, 5)]\n\033[0m")
dados = [(0,1), (1, 2), (2, 3), (3,4), (4, 5)]

print(f'\033[32m{list(zip(*dados))}')

# ---------------- ↓ exemplos mais complexos ↓ -------------

print(f'\n\033[37m-------------- ↓\033[34m imprimindo a maior nota por aluno\033[37m↓ ---------------'
      f'---\n\033[0m')

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

print(f'\033[37mnotas dos alunos: \033[34m{list(zip(alunos, prova1, prova2))}')

# ---------------- ↓ exemplos mais complexos ↓ -------------

final = {dado[0]:max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(f'\033[37mA maior nota por aluno foi: \033[32m{final}')

print(f'\n\033[37m---------- ↓\033[34m imprimindo a maior nota por aluno com cores \033[37m↓ --------'
      f'---\n\033[0m')

# Dados dos alunos
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

# Associe cada aluno a uma cor ANSI
cores_alunos = {
    'maria': "\033[31m",  # Vermelho
    'pedro': "\033[32m",  # Verde
    'carla': "\033[33m",  # Amarelo
}

# Certifique-se de redefinir a cor após a impressão
reset_cor = "\033[0m"

# -------------------------- ↓ Forma 1 ↓ -----------------------

print(f'\033[36m------------------------------ ↓ Forma 1 ↓ ---------------------------\033[0m\n')
# Crie o dicionário final com as notas máximas
final = {aluno: max(nota1, nota2) for aluno, nota1, nota2 in zip(alunos, prova1, prova2)}
print("final = {aluno: max(nota1, nota2) for aluno, nota1, nota2 in zip(alunos, prova1, prova2)}")

# Imprima o dicionário final com cores
print(f'\033[37mA maior nota por aluno foi:')
for aluno, nota in final.items():
    cor = cores_alunos.get(aluno, "\033[0m")  # Obtém a cor associada ao aluno
    print(f'{cor}{aluno}: {nota}{reset_cor}')

# ---------------- ↓ Forma 2 ↓ -------------

print(f'\033[36m------------------------------ ↓ Forma 2 ↓ ---------------------------\033[0m\n')
final = {dado[0]:max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print("final = {dado[0]:max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}\n")

# Imprima o dicionário final com cores
print(f'\033[37mA maior nota por aluno foi:')
for aluno, nota in final.items():
    cor = cores_alunos.get(aluno, "\033[0m")  # Obtém a cor associada ao aluno
    print(f'{cor}{aluno}: {nota}{reset_cor}')

# ---------------- ↓ Forma 3 - Map ↓ -------------

print(f'\033[36m--------------------------- ↓ Forma 3 - Map ↓ ------------------------\033[0m\n')

final = zip(alunos, map(lambda note: max(note), zip(prova1, prova2)))
print("final = zip(alunos, map(lambda note: max(note), zip(prova1, prova2)))\n")

# Imprima o dicionário final com cores
print(f'\033[37mA maior nota por aluno foi:')
for aluno, nota in final:
    cor = cores_alunos.get(aluno, "\033[0m")  # Obtém a cor associada ao aluno
    print(f'{cor}{aluno}: {nota}{reset_cor}')
