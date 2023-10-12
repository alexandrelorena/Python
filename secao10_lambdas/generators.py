"""
Generator Expression  => Tuple Comprehension
- usa ()
"""
from sys import getsizeof

# ------------------------------ ↓ Generator Expression ↓ -------------------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ Generators ↓'.center(70)}\033[33m\n{'-' * 70}\033[0m")

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Daniel']
print("nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Daniel']")

# ------------------------------ ↓ any() com generators ↓ -------------------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ any() com generators ↓'.center(70)}\033[33m\n{'-' * 70}\033[0m")

print("print(any(nome[0] == 'C' for nome in nomes))")
print(any(nome[0] == 'C' for nome in nomes))  # any()

# ------------------------------ ↓ List Comprehension ↓ -------------------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ List Comprehension ↓'.center(70)}\033[33m\n{'-' * 70}\033[0m")

# List Comprehension
print("nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Daniel']")
print("res = [nome[0] == 'C' for nome in nomes]")
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)
print(getsizeof(res))

# ------------------------------ ↓ Generators e getsizeof() ↓ -------------------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ Generators e getsizeof() ↓'.center(70)}\033[33m\n{'-' * 70}\033[0m")

# Generator  =>  + performático (gasta menos recursos da máquina)
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)
print(getsizeof(res))

print(getsizeof('Geek'))
#  getsizeof() retorna a quantidade de bytes em memória, do elemento passado como parâmetro.
print(getsizeof('University'))
print(getsizeof(9))
print(getsizeof(91))
print(getsizeof(92345668823))
print(getsizeof(True))

# ------------------------------ ↓ List Comprehension - gerando lista de números ↓ -------------------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ List Comprehension - gerando lista de números ↓'.center(70)}\033[33m\n"
      f"{'-' * 70}"f"\033[0m")

list_comp = getsizeof([x * 10 for x in range(1000)])
print("list_comp = getsizeof([x * 10 for x in range(1000)])")

# ------------------------------ ↓ Set Comprehension - gerando lista de números ↓ -------------------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ Set Comprehension - gerando lista de números ↓'.center(70)}\033[33m\n{'-' * 70}"
      f"\033[0m")

set_comp = getsizeof({x * 10 for x in range(1000)})
print("set_comp = getsizeof({x * 10 for x in range(1000)})")

# --------------------------- ↓ Dictionary Comprehension - gerando lista de números ↓ ----------------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ Dictionary Comprehension - gerando lista de números ↓'.center(70)}"
      f"\033[33m\n{'-' * 70}\033[0m")

dic_comp = getsizeof({x: x * 10 for x in range(1000)})
print("dic_comp = getsizeof({x: x * 10 for x in range(1000)})")

# --------------------------- ↓ Generator Expression - gerando lista de números ↓ ----------------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ Generators - gerando lista de números ↓'.center(70)}\033[33m\n{'-' * 70}"
      f"\033[0m")

gen = getsizeof(x * 10 for x in range(1000))
print("gen = getsizeof(x * 10 for x in range(1000))")

# --------------------------- ↓ Para fazer a mesma tarefa gastamos em memória: ↓ ----------------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ Para fazer a mesma tarefa gastamos em memória: ↓'.center(70)}\033[33m\n"
      f"{'-' * 70}\033[0m")

print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dic_comp} bytes')
print(f'Generator Expression: {gen} bytes')

# --------------------------- ↓ Iterando no Generator Expression- ↓ ----------------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ Iterando no Generator Expression ↓'.center(70)}\033[33m\n"f"{'-' * 70}\033[0m")

"""gen = (x * 10 for x in range(100))
print(gen)
print(type(gen))

for num in gen:
    print(num, end=", ")"""

gen = (x * 10 for x in range(100))

# Inicialize um contador
count = 0

# Itera sobre o gerador
for num in gen:
    print(num, end=", ")
    count += 1  # count = count + 1

    # Verifique se já imprimiu 10 valores na linha
    if count == 10:
        print()  # Imprime uma nova linha
        count = 0  # Reinicia o contador
