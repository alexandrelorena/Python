"""
Dunder Name e Dunder Main

Dunder -> Dobble Under

Dunder Name -> __name__
    - arquivo executado via importação, o nome dele passa a ser o nome do arquivo
Dunder Main -> __main__
    - significa principal.

- São utilizados para criar funções, atributos, propriedades e etc, utilizando Double Under
para não gerar conflito com os nomes desses elementos na programação.

"""
from colorama import Fore, Style

from secao08_funcoes.funcoes_com_parametros_dunder import soma_impares, cantar_parabens

print(f"\033[33m{'-' * 80}\n\033[94m{'↓ Dunder Name e Dunder Main ↓'.center(80)}\033[33m\n"
      f"{'-' * 80}\033[0m\n")

print(Fore.CYAN + '------------------ ↓ Usando a função importada soma_impares ↓ ------------------\n')

print(Fore.LIGHTGREEN_EX + "from secao08_funcoes.funcoes_com_parametros_dunder import soma_impares, cantar_parabens" +
      Fore.BLACK + " >> importando módulo e funções\n")

print(Fore.BLUE + "print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9])) >> " + Fore.MAGENTA + f'soma dos números ímpares >>'
                  f' ' + Fore.BLACK + f"{soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9])}")

print(Fore.CYAN + '\n----------------- ↓ Usando a função importada cantar_parabens ↓ ----------------')

print(Style.RESET_ALL)

print(Fore.BLUE + cantar_parabens("Alexandre"))
print(Style.RESET_ALL)
"""import primeiro
import segundo"""
