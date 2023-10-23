"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo

"""

from colorama import Fore

print(f"\033[33m{'-' * 80}\n\033[94m{'↓ Seek e Cursors ↓'.center(80)}\033[33m\n"
      f"{'-' * 80}\033[0m\n")

print(Fore.CYAN + '---------- ↓ Imprimindo o texto de um arquivo ↓ ----------')
print(Fore.YELLOW)
arquivo = open('../../pythonProject/texto.txt', 'r', encoding='utf-8')
arquivo = open('../../pythonProject/texto.txt', 'r', encoding='utf-8')

print(arquivo.read())

print(Fore.CYAN + '\n---------- ↓ Movimentando o cursor pelo arquivo com a função seek() ↓ ----------')

print(arquivo.read())
arquivo.seek(0)
print(arquivo.read())
arquivo.seek(0)
print(arquivo.read())

