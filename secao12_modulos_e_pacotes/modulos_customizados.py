"""
Modulos Customizados

"""

import secao08_funcoes.funcoes_com_parametro as funcs
import secao12_modulos_e_pacotes.importando_modulo as impm
from secao10_lambdas.map import cidades, c_para_f

print(f"\033[33m{'-' * 80}\n\033[94m{'↓ Modulos Customizados ↓'.center(80)}\033[33m\n"
      f"{'-' * 80}\033[0m\n")

print(f'\033[37m------------------------ ↓ \033[30mMódulo com apenas 1 função\033[37m ↓ ------------------------'
      f'\n\033[0m')

print("\033[35mimport secao12_modulos_e_pacotes.importando_modulo as impm\n\n\033[34mprint(impm.soma_impares([1, 2, 3, "
      "4, 5, 6, 7, 8, 9"
      "]))\033[36m >>", end=' ')

print(impm.soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# ---------------------------------- ↓ Todo o módulo: secao08_funcoes.funcoes_com_parametro ↓ --------------------------

print(f'\n\033[37m----------- ↓ \033[30mTodo o módulo: secao08_funcoes.funcoes_com_parametro\033[37m ↓ -----------'
      f'\033[0m')

print("\n\033[35mimport secao08_funcoes.funcoes_com_parametro as funcs\n\n\033[34mfuncs.lista\033[36m >>", end=' ')
print(funcs.lista)

print("\n\033[34mprint(funcs.tupla)\033[36m >>", end=' ')
print(funcs.tupla)

print("\n\033[34mprint(funcs.soma_impares(funcs.lista))\033[36m >>", end=' ')
print(funcs.soma_impares(funcs.lista))
print("\n\033[34mprint(funcs.lista)\033[36m >>", end=' ')
print(funcs.lista)

# ------------------------------------------ ↓ Todo o módulo: secao10_lambdas.map ↓ ----------------------------------

print(f'\n\033[37m-------------------- ↓ \033[30mTodo o módulo: secao10_lambdas.map\033[37m ↓ --------------------'
      f'\033[0m')

print("\n\033[35mfrom secao10_lambdas.map import cidades, c_para_f\n\n\033[34mprint(list(map(c_para_f, cidades)))"
      "\033[36m\n")
print(list(map(c_para_f, cidades)))
print("\n\033[35mfrom secao10_lambdas.map import cidades, c_para_f\n\n\033[34mfor cidade in cidades:\n    temperatura_"
      "fahrenheit = c_para_f(cidade)\n    print(temperatura_fahrenheit)\n\033[36m")
for cidade in cidades:
    temperatura_fahrenheit = c_para_f(cidade)
    print(temperatura_fahrenheit)
