"""
trabalhando com Módulos Built-in (módulos integrados que já vem instalados no Python).

________________________
|Python|Módulos builtin|
------------------------

----------------------------- ↓ Alias ↓ ----------------------------

import random as rdm
print(rdm.random())

----------------------------- ↓ import com * (asterisco) ↓ ----------------------------

from random import *
print(random())

# importando todo o módulo

----------------------------- ↓ Alias para função ↓ ----------------------------

from random import randint as rdi

print(rdi(5, 89))

----------------------------- ↓ Alias para duas ou mais funções ↓ ----------------------------

from random import randint as rdi, random as rdm

print(rdi(5, 89)) >> 69
print(rdm()) >> 0.2027145447858968

----------------------------- ↓ Utilizando tuple ↓ ----------------------------

from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random()) >> 0.9132111123122153

print(randint(3, 7)) >> 5

lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista) >> ['Geek', 'University', 'Python']

print(choice('University')) >> n

"""
import random as rdm  # 'as' atribui o alias (apelido) ao módulo

print(f"\033[33m{'-' * 80}\n\033[94m{'↓ trabalhando com Módulos Built-in ↓'.center(82)}\033[33m\n{'-' * 80}"
      f"\033[0m\n")

# ---------------------------------------------- ↓ Utilizando alias (apelidos) ↓ --------------------------------------

print(f'\033[37m------------------------ ↓ \033[30mUtilizando alias (apelidos)\033[37m ↓ -----------------------'
      f'\n\033[0m')

print("\033[35mimport random as rdm\n\n\033[34mprint(rdm.random())\033[36m >>", end=' ')
print(rdm.random())

# ---------------------------------------------- ↓ Importando com * (asterisco) ↓ --------------------------------------

print(f'\n\033[37m----------------------- ↓ \033[30mImportando com * (asterisco)\033[37m ↓ -----------------------'
      f'\n\033[0m')

from random import *

print("\033[35mfrom random import *\n\n\033[34mprint(random())\033[36m >>", end=' ')
print(random())

# ---------------------------------------------- ↓ Utilizando alias para função ↓ --------------------------------------

print(f'\n\033[37m----------------------- ↓ \033[30mUtilizando alias para função\033[37m ↓ -----------------------'
      f'\n\033[0m')

from random import randint as rdi

print("\033[35mfrom random import randint as rdi\n\n\033[34mprint(rdi(5, 89))\033[36m >>", end=' ')
print(rdi(5, 89))

# ----------------------------- ↓ Utilizando alias para 2 ou mais funções ↓ ------------------------------

print(f'\n\033[37m----------------- ↓ \033[30mUtilizando alias para 2 ou mais funções\033[37m ↓ -----------------'
      f'\n\033[0m')

from random import randint as rdi, random as rdm

print("\033[35mfrom random import randint as rdi, random as rdm\n\n\033[34mprint(rdi(5, 89))\033[36m >>", end=' ')
print(rdi(5, 89))
print("\033[35m\033[34mprint(rdm())\033[36m >>", end=' ')
print(rdm())

# ------------------------------------------------ ↓ Utilizando tuple ↓ ---------------------------------------------

print(f'\n\033[37m----------------------------- ↓ \033[30mUtilizando tuple\033[37m ↓ ----------------------------'
      f'\n\033[0m')

# Usar tuple para colocar múltiplos imports de um mesmo módulo:

print("\033[35mfrom random import (    \n    random,    \n    randint,    \n    shuffle,    \n    choice\n)\n\n"
      "\033[36m", end='')

print("\033[32mprint(random())\033[30m >>", end=' ')
print(random())

print("\n\033[34mprint(randint(3, 7))\033[36m >>", end=' ')
print(randint(3, 7))

print("\n\033[37mlista = ['Geek', 'University', 'Python']\nshuffle(lista)\nprint(lista)\033[31m >>", end=' ')
lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)

print("\n\033[0mprint(choice('University'))\033[32m >>", end=' ')
print(choice('University'))
