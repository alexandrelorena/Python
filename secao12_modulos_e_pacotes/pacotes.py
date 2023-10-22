"""
Pacotes

- Módulo >> arquivo Pythonque podem ter diversas funções para utilizar;
- Pacotes são diretórios contendo coleção de módulos

"""

from colorama import Fore

from geek import geek1, geek2

from geek.university import geek3, geek4

from geek.geek1 import funcao1

from geek.university.geek4 import funcao4

print(f"\033[33m{'-' * 80}\n\033[94m{'↓ Pacotes ↓'.center(80)}\033[33m\n"
      f"{'-' * 80}\033[0m\n")

print(Fore.CYAN + '-------------------------- ↓ Trabalhandp com Pacotes ↓ -------------------------\n')

print(Fore.LIGHTGREEN_EX + "from geek import geek1" + Fore.YELLOW + " >> importando pacote\n")

print(Fore.BLUE + "print(geek1.pi)", end=' >> ' + Fore.CYAN + f'pi = {str(geek1.pi)}' + Fore.LIGHTBLUE_EX +
                  ' >> pi está no arquivo geek1'"\n\n")  # convertido .float  para string

# print(Fore.CYAN + f'pi = {str(geek1.pi)}' + Fore.LIGHTBLUE_EX + ' >> pi está no arquivo geek1'"\n")

print(Fore.LIGHTGREEN_EX + f'a + b = {geek1.funcao1(4, 6)}' + Fore.MAGENTA + ' >> função1 está no arquivo geek1\n')

print(Fore.LIGHTCYAN_EX + f'Imprimindo a variável curso: ' + Fore.BLUE + geek2.curso + '\n')

print(Fore.BLUE + f'Imprimindo a função2(): ' + Fore.LIGHTCYAN_EX + geek2.funcao2() + '\n')

print(Fore.LIGHTCYAN_EX + f'Imprimindo as funções geek3 + geek4: ' + Fore.BLUE + geek3.funcao3() + ' ' +
      geek4.funcao4() + '\n')

print(Fore.LIGHTCYAN_EX + "from geek.geek1 import funcao1" + Fore.YELLOW + " >> importando apenas a função1 do arquivo "
                          "geek1 do pacote geek >> " + Fore.BLUE + (str(funcao1(6, 9))) + "\n")

print(Fore.LIGHTCYAN_EX + "from geek.university.geek4 import funcao4" + Fore.YELLOW + " >> importando apenas a função4"
                          " do arquivo geek4 do pacote university que está dentro do pacote geek >> " + Fore.BLUE +
      (str(funcao4()) + "\n"))
