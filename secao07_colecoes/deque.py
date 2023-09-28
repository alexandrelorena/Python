
"""
Módulo Collections - Deque

Collections >> High-performance Container Datetypes

"""
# Importando

from collections import deque

# Criando deques

deq = deque('geek')

print(deq)

# Adicionando elementos no deq

deq.append('y')  # adiciona no final

print(deq)

deq.appendleft('k')  # adiciona no começo

print(deq)

#  Removendo elementos

print(deq.pop())  # Remove e retorna o último elemento

print(deq)

print(deq.popleft())  # Remove e retorna o primeiro elemento

print(deq)
