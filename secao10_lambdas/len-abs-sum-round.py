"""
Len => Retorna o tamanho (número de itens) de um iterável

Abs => Retorna o valor absoluto de um número Inteiro ou Real (sem o sinal)

Sum => Recebe como parâmetro um iterável, podendo receber um valor inicial e retorna
a soma total dos elementos, incluindo o valor inicial.
obs: o valor inicial default é 0 (zero).
- Não funciona com string.

Round => Retorna um número arredondado para n dígito de precisão após a casa decimal.
Se a precisão não for informada, retorna o inteiro mais próximo da entrada.

"""
# ------------------------------ ↓ len-abs-sum-round ↓ ----------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ len-abs-sum-round ↓'.center(70)}\033[33m\n{'-' * 70}\033[0m\n")

# ------------------------------------- ↓ len() ↓ -----------------------------------

print(f'\033[37m----------------------------------- ↓ \033[34mlen() \033[37m↓ -------------------------------'
      f'---\n\033[0m')

# Retorna o tamanho (número de itens) de um iterável

# print('Geek University'.__len__())  => Dunder len => é isso que a funçao len() faz

print("\033[37mGeek University => " + str(len('Geek University')), end=' => ')
print(type('Geek University'))

print("\033[36mlista => " + str(len([1, 2, 3, 4, 5])), end=' => ')
print(type([1, 2, 3, 4, 5]))

print("\033[35mtupla => " + str(len((1, 2, 3, 4, 5))), end=' => ')
print(type((1, 2, 3, 4, 5)))

print("\033[34mconjunto (set) => " + str(len({1, 2, 3, 4, 5})), end=' => ')
print(type({1, 2, 3, 4, 5}))

print("\033[33mdicionario => " + str(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})), end=' => ')
print(type({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

print("\033[31mrange => " + str(len(range(0, 10))), end=' => ')
print(type(range(0, 10)))

# ------------------------------------- ↓ abs() ↓ -----------------------------------

print(f'\n\033[37m----------------------------------- ↓ \033[34mabs() \033[37m↓ -------------------------------'
      f'---\n\033[0m')

# Retorna o valor absoluto de um número Inteiro ou Real (sem o sinal)
print(f'\033[37mabs() de -5 => ' + str(abs(-5)), end=' => ')
print(type(-5))

print(f'\033[36mabs() de 5 => ' + str(abs(5)), end=' => ')
print(type(5))

print(f'\033[35mabs() de 3.14 => ' + str(abs(-5)), end=' => ')
print(type(3.14))

print(f'\033[34mabs() de -3.14 => ' + str(abs(-3.14)), end=' => ')
print(type(-3.14))

# ------------------------------------- ↓ sum() ↓ -----------------------------------

print(f'\n\033[37m------------------------------ ↓ \033[34msum() - lista \033[37m↓ ----------------------------'
      f'---\n\033[0m')

# Recebe como parâmetro um iterável, podendo receber um valor inicial e retorna
# a soma total dos elementos, incluindo o valor inicial.
# obs: o valor inicial default é 0 (zero).

# ------------------------------------- ↓ lista ↓ -----------------------------------

print(f'\033[37mlista sem valor inicial => ' + str(sum([1, 2, 3, 4, 5])), end=' => ')
print(type([1, 2, 3, 4, 5]))

print(f'\033[36mlista com valor inicial + 5 => ' + str(sum([1, 2, 3, 4, 5], 5)), end=' => ')
print(type([1, 2, 3, 4, 5]))

print(f'\033[35mlista com valor inicial - 5 => ' + str(sum([1, 2, 3, 4, 5], -5)), end=' => ')
print(type([1, 2, 3, 4, 5]))

print(f'\n\033[37m------------------------------ ↓ \033[34msum() - tupla \033[37m↓ ----------------------------'
      f'---\n\033[0m')

# ------------------------------------- ↓ tupla ↓ ------------------------------------

print(f'\033[37mtupla sem valor inicial => ' + str(sum((1, 2, 3, 4, 5))), end=' => ')
print(type((1, 2, 3, 4, 5)))

print(f'\033[36mtupla com valor inicial + 5 => ' + str(sum((1, 2, 3, 4, 5), 5)), end=' => ')
print(type((1, 2, 3, 4, 5)))

print(f'\033[35mtupla com valor inicial - 5 => ' + str(sum((1, 2, 3, 4, 5), -5)), end=' => ')
print(type((1, 2, 3, 4, 5)))

print(f'\n\033[37m----------------------------- ↓ \033[34msum() - conjunto \033[37m↓ --------------------------'
      f'---\n\033[0m')

# ------------------------------------ ↓ conjunto ↓ ----------------------------------

print(f'\033[37mconjunto (set) sem valor inicial => ' + str(sum({1, 2, 3, 4, 5})), end=' => ')
print(type({1, 2, 3, 4, 5}))

print(f'\033[36mconjunto (set) com valor inicial + 5 => ' + str(sum({1, 2, 3, 4, 5}, 5)), end=' => ')
print(type({1, 2, 3, 4, 5}))

print(f'\033[35mconjunto (set) com valor inicial - 5 => ' + str(sum({1, 2, 3, 4, 5}, -5)), end=' => ')
print(type({1, 2, 3, 4, 5}))

print(f'\n\033[37m---------------------------- ↓ \033[34msum() - dicionario \033[37m↓ -------------------------'
      f'---\n\033[0m')

# ----------------------------------- ↓ dicionario ↓ ---------------------------------

print(f'\033[37mdicionario sem valor inicial => ' + str(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values())),
      end=' => ')
print(type({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

print(f'\n\033[36mdicionario sem valor inicial => ' + str(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()) + 5),
      end=' => ')
print(type({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

print(f'\n\033[35mdicionario sem valor inicial => ' + str(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()) - 5),
      end=' => ')
print(type({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

# ------------------------------------- ↓ round() ↓ -----------------------------------

print(f'\n\033[37m------------------------------ ↓ \033[34mround() - lista \033[37m↓ ----------------------------'
      f'---\n\033[0m')

print(round(10.2))  # número inteiro

print(round(10.5))  # número inteiro

print(round(10.6))  # número inteiro

print(round(1.2121212121, 2))  # número real

print(round(1.21999999, 2))  # número real
