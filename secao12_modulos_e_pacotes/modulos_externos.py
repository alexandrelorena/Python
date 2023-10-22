"""
Módulos externos

instalação:
      pip instal nome_do_modulo

Utilizamos o gerenciados de pacotes  chamado Pip - Python Installer Package

colorama > permite impressão de textos coloridos no terminal

      from colorama import init
            init()
      from colorama import Fore, Back, Style
            print(Fore.RED + 'Geek University')
      Geek University
            print(Fore.GREEN + 'Geek University')
      Geek University
            print(Fore.BLUE + 'Geek University')
      Geek University

            print(Style.RESET_ALL) # reseta estilo aplicado
"""
from colorama import init, Fore, Back, Style

print(f"\033[33m{'-' * 80}\n\033[94m{'↓ Modulos Externos ↓'.center(80)}\033[33m\n"
      f"{'-' * 80}\033[0m\n")

print(Fore.CYAN + '------------------------------ ↓ Colorama - Fore ↓ -----------------------------\n')

print("\033[35mfrom colorama import init, Fore\n\n\033[34minit()\n\nprint(Fore.MAGENTA + 'Geek University'), \n"
      "print(Fore.CYAN + 'Geek University')\nprint(Fore.LIGHTGREEN_EX + 'Geek University')]))\n\033[36m")

init()

print(Fore.MAGENTA + 'Geek University')
print(Fore.CYAN + 'Geek University')
print(Fore.LIGHTGREEN_EX + 'Geek University')

print(Fore.CYAN + '\n------------------------ ↓ Colorama - Fore, Back, Style ↓ ----------------------\n')

print(Fore.BLACK + 'WHITE', end=', ')
print(Fore.RED + 'RED', end=', ')
print(Fore.GREEN + 'GREEN', end=', ')
print(Fore.YELLOW + 'YELLOW', end=', ')
print(Fore.BLUE + 'BLUE', end=', ')
print(Fore.MAGENTA + 'MAGENTA', end=', ')
print(Fore.CYAN + 'CYAN', end=', ')
print(Fore.WHITE + 'GRAY')
print()
print(Fore.BLACK + 'Style.RESET_ALL', Fore.RED + '>> Remove todos os estilos')
print()
print(Fore.GREEN + "Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.")
print()
print(Fore.CYAN + "Style: DIM, NORMAL, BRIGHT, RESET_ALL")
print()
print(Back.BLACK, Fore.WHITE + 'Background WHITE', end=' ')
print(Back.MAGENTA, Fore.BLACK + 'Background MAGENTA', end=' ')
print(Back.GREEN, Fore.BLACK + 'Background GREEN', end=' ')
print(Back.WHITE, Fore.BLACK + 'Background GRAY', end=' ')
print(Style.RESET_ALL)
print()
print(Back.BLUE, Fore.BLACK + 'Background BLUE', end=' ')
print(Back.RED, Fore.BLACK + 'Background RED', end=' ')
print(Back.CYAN, Fore.BLACK + 'Background CYAN', end=' ')
print(Back.YELLOW, Fore.BLACK + 'Background YELLOW', end=' ')
print(Style.RESET_ALL)
print()
print(Style.DIM, Fore.BLACK + 'Style.DIM', end=' |')
print(Style.NORMAL, Fore.BLACK + 'Style.NORMAL', end=' |')
print(Style.BRIGHT, Fore.BLACK + 'Style.BRIGHT', end=' ')
