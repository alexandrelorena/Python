"""
Módulo Random

- Em Python, módulos são outros arquivos Python.

- Módulo Random possui várias funções para gerar números pseudo-aleatórios.

"""

import random

#  Forma 1 > NÃO RECOMENDADO >> Importando todo o módulo (todas as funções, atributos, classes e propriedades)

#  Forma 2 > Importando uma função específica do módulo

# ---------------------------------------------- ↓ Módulo Random ↓ --------------------------------------

print(f"\033[33m{'-' * 80}\n\033[94m{'↓ Módulo Random ↓'.center(82)}\033[33m\n{'-' * 80}"
      f"\033[0m\n")

# ------------------------- ↓ Forma NÃO RECOMENDADO >> Importando todo o módulo)  ↓ -------------------------

print(f'\033[37m------------- ↓ \033[30mForma NÃO RECOMENDADA >> Importando todo o módulo\033[37m ↓ ------------'
      f'\n\033[0m')

random_value = random.random()

print("\033[35mprint(random.random()) >> \033[36m", random_value)

print("\n\033[32mGera um número pseudo-aleatório entre 0 e 1")

# ---------------------------- ↓ Forma RECOMENDADA > Importando uma função específica do módulo  ↓ ---------------------

print(f'\n\033[37m------ ↓ \033[30mForma RECOMENDADA > Importando uma função específica do módulo\033[37m ↓ ------'
      f'\n\033[0m')

from random import random  # import deve ser inserido no início do arquivo!

print("\033[35mfrom random import random \n\n\033[34mfor i in range(10): \n    print(random())\n\033[36m")

print("\033[32mGera 10 números reais pseudo-aleatórios entre 0 e 1\n\033[36m")

for i in range(10):
    print(random())

# --------------------------------------------- ↓ Função uniform()  ↓ --------------------------------------------

print(f'\n\033[37m----------------------------- ↓ \033[30mFunção uniform()\033[37m ↓ -----------------------------'
      f'\n\033[0m')

from random import uniform  # import deve ser inserido no início do arquivo!

print("\033[35mfrom random import uniform \n\n\033[34mfor i in range(10): \n    print(uniform(3, 7))\n\033[36m")

print("\033[32mGera 10 números reais pseudo-aleatórios entre 3 e 7 >> o número após a vírgula não é incluído\n\033[36m")

for i in range(10):
    print(uniform(3, 7))

# --------------------------------------------- ↓ Função randint() ↓ --------------------------------------------

print(f'\n\033[37m----------------------------- ↓ \033[30mFunção randint()\033[37m ↓ -----------------------------'
      f'\n\033[0m')

from random import randint  # import deve ser inserido no início do arquivo!

print("\033[35mfrom random import randint \n\n\033[34mfor i in range(6): \n    if i < 5:\n        print(randint(1, 61),"
      " end=', ')\n    else:\n        print(randint(1, 61), end=' ')\n\033[36m")

print("\033[32mGera 6 valores reais pseudo-aleatórios entre os valores estabelecidos.\n\033[36m")

#  Gerador de apostas na Mega Sena

for i in range(6):
    if i < 5:  # verificação condicional para imprimir a vírgula enquanto não for a última iteração.
        print(randint(1, 61), end=', ')
    else:
        print(randint(1, 61), end=' ')

# --------------------------------------------- ↓ Função choice() ↓ --------------------------------------------

print(f'\n\033[37m----------------------------- ↓ \033[30mFunção choice()\033[37m ↓ ------------------------------'
      f'\n\033[0m')

#  Jogadas

from random import choice  # import deve ser inserido no início do arquivo!

jogadas = ['pedra', 'papel', 'tesoura']

print("\033[35mfrom random import choice \n\n\033[34mjogadas = ['pedra', 'papel', 'tesoura']\n\nprint(choice(jogadas))"
      "\033[36m >>", end='')

print("\033[36m", choice(jogadas))

# choice() em strings

print("\n\033[32mMostra um valor aleatório entre um iterável.\n\033[36m")

print(choice('Geek University'))

# --------------------------------------------- ↓ Função shuffle() ↓ --------------------------------------------

print(f'\n\033[37m----------------------------- ↓ \033[30mFunção shuffle()\033[37m ↓ -----------------------------'
      f'\n\033[0m')

from random import shuffle

# embaralhando cartas

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10']

print(cartas)

shuffle(cartas)

print(cartas)

print(cartas[10])