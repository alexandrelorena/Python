"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo

streaming -> Ao abrir um arquivo com a função open(), é criada uma conexão entre o arquivo no disco do computador e o
nosso programa.
Para fechar essa conexão, utilizamos a função close().
"""

from colorama import Fore

print(f"\033[33m{'-' * 80}\n\033[94m{'↓ Seek e Cursors ↓'.center(80)}\033[33m\n"
      f"{'-' * 80}\033[0m\n")

print(Fore.CYAN + '---------------------- ↓ Abrindo um arquivo um arquivo ↓ -----------------------\n')

print(Fore.WHITE + f'arquivo = open(../../pythonProject/texto.txt', 'r', 'encoding=utf-8')

arquivo = open('../../pythonProject/texto.txt', 'r', encoding='utf-8')

print()

print(Fore.CYAN + '---------------------------- ↓ Lendo um arquivo ↓ ------------------------------\n')

print(Fore.WHITE + f'arquivo.read()')

print()

print(Fore.YELLOW + arquivo.read())

print(Fore.CYAN + '\n---------- ↓ Movimentando o cursor pelo arquivo com a função seek() ↓ ----------\n')

print(Fore.WHITE + f'arquivo.seek(0) => # cursor setado para posição 0 do texto\n')

arquivo.seek(0)  # cursor setado para posição 0
print(Fore.YELLOW + arquivo.read())  # relendo o arquivo
print()

print(Fore.WHITE + f'arquivo.seek(25) => # cursor setado para posição 25 do texto\n')

arquivo.seek(25)  # cursor setado para posição 25

print(Fore.BLUE + arquivo.read())  # relendo o arquivo

print(Fore.WHITE + f'\narquivo.seek(50) => # cursor setado para posição 50 do texto\n')

arquivo.seek(50)  # cursor setado para posição 50

print(Fore.GREEN + arquivo.read())  # relendo o arquivo

print(Fore.CYAN + '\n---------------- ↓ readline() -> função que lê linha a linha ↓ -----------------\n')

arquivo.seek(0)  # cursor setado para posição 0

print(Fore.WHITE + f'arquivo.readline() => # lê a primeira linha\n')
print(Fore.BLACK + arquivo.readline())

print(Fore.WHITE + f'arquivo.readline() => # lê a próxima linha\n')
print(Fore.BLUE + arquivo.readline())

print(Fore.WHITE + f'arquivo.readline() => # lê a próxima linha\n')
print(Fore.BLUE + arquivo.readline())

print(Fore.WHITE + f'arquivo.readline(95) => # lê 95 caracteres da linha\n')
print(Fore.GREEN + arquivo.readline(95))

arquivo.seek(0)  # cursor setado para posição 0

print(Fore.MAGENTA + f'\ncolocando o conteúdo do arquivo.readline() na variável ret\n')
print(Fore.BLUE + f'ret = arquivo.readline()\n')

ret = arquivo.readline()

print(Fore.MAGENTA + f'imprimindo o tipo da variável ret\n')

print(Fore.BLUE + f'print(type(ret)) =>> ' + Fore.WHITE + str(type(ret)) + '\n')

print(Fore.MAGENTA + f'imprimindo o conteúdo da variável ret\n')

print(Fore.BLUE + f'print(type(ret)) =>> ' + Fore.WHITE + ret)

print(Fore.CYAN + '-------------------- ↓ imprimindo o conteúdo em uma lista ↓ --------------------\n')

print(Fore.MAGENTA + f'imprimindo o conteúdo em uma lista\n')

print(Fore.BLUE + f'print(ret.split(' ')) =>> ', end='' + Fore.YELLOW)

print(f'{(ret.split(" "))}')


arquivo.seek(0)  # cursor setado para posição 0

print(Fore.MAGENTA + f'\nlimitar a quantidade de caracteres que serão lidos.\n')

print(Fore.BLUE + f'print(arquivo.read(40)) =>> ', end='' + Fore.YELLOW)
print(arquivo.read(40))

print(Fore.MAGENTA + f'\ncolocando o "arquivo" .readlines() na variável linhas\n')

print(Fore.BLUE + f'linhas = arquivo.readlines() =>> ', end='' + Fore.YELLOW)

linhas = arquivo.readlines()

print(Fore.MAGENTA + f'contar número de linhas\n')

print(Fore.BLUE + f'print(len(linhas)) =>> ', end='' + Fore.YELLOW)
print(len(linhas))

print(Fore.CYAN + '\n---------------- ↓ verificando/fechando conexão com o arquivo ↓ ----------------\n')

print(Fore.MAGENTA + f'verifica se a conexão com o arquivo está fechada\n')
print(Fore.BLUE + f'arquivo.closed =>> ', end='' + Fore.YELLOW)
print(arquivo.closed)  # verifica se o arquivo está aberto ou fechado

print(Fore.MAGENTA + f'\nfechar conexão com o arquivo\n')
print(Fore.BLUE + f'arquivo.close()')
arquivo.close()

print(Fore.MAGENTA + f'\nverifica se a conexão com o arquivo está fechada\n')
print(Fore.BLUE + f'arquivo.closed =>> ', end='' + Fore.YELLOW)
print(arquivo.closed)
