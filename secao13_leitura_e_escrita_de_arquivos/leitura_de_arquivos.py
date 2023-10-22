"""
Leitura de arquivos

open() -> função integrada
- Na forma mais simples de utilização é passada apenas um parâmetro de entrada (nome do arquivo a ser lido).
- Essa função retorna um _io.TextIOWrapper.

OBS: Por padrão, a função open() abre o arquivo para leitura. Se o arquivo não existir, dará o erro FileNotFoundError.

<_io.TextIOWrapper name='../../pythonProject/texto.txt' mode='r' encoding='cp1252'>

mode r -> read() -> ler - Modo de leitura

OBS 2:
"""
from colorama import Fore
print(f"\033[33m{'-' * 80}\n\033[94m{'↓ Leitura de arquivos ↓'.center(80)}\033[33m\n"
      f"{'-' * 80}\033[0m\n")

print(Fore.CYAN + '------------------ ↓ Usando a função integrada open() ↓ ------------------\n')

arquivo = open('../../pythonProject/texto.txt', 'r', encoding='utf-8')

print(Fore.BLUE + "arquivo = open('../../pythonProject/texto.txt', 'r') >> " + Fore.MAGENTA + f'abrindo arquivo\n')

print(Fore.CYAN + '------------------ ↓ Usando a função integrada read() ↓ ------------------\n')

print(Fore.YELLOW + 'print(Fore.BLUE + arquivo.read())' + Fore.BLUE + f' => lendo o arquivo\n')

print(Fore.MAGENTA + f'{arquivo.read()}')

print(Fore.YELLOW)
print(f'{arquivo}' + Fore.BLUE + f' => imprimindo a variável "arquivo"')

print(Fore.YELLOW)
print(F'{type(arquivo)}' + Fore.BLUE + f' => imprimindo tipo do arquivo')

ret = arquivo.read()
print(Fore.YELLOW)
print(F'{type(ret)}' + Fore.BLUE + f' => imprimindo tipo do arquivo')
