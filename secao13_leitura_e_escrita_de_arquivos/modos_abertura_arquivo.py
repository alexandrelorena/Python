"""
Modos de abertura em arquivos

r -> abre para leitura - padrão
w -> abre para escrita - sobrescreve caso o arquivo já exista
x -> abre para escrita - somente se o arquivo não existir. caso o arquivo exista, gera FileExistsError.

http://docs.python.org/3/library/functions.html#open

"""

from colorama import Fore, Back, init

# -------------------------------------------- ↓ Bloco título ↓ --------------------------------------------

# Inicialize o Colorama
init(autoreset=True)

# Cor de fundo que você deseja
cor_de_fundo = Back.BLUE

# Altura do fundo (número de linhas)
altura_do_fundo = 1

# Largura da linha
largura_da_linha = 145

# Imprime as linhas de início com a cor amarela
print(f"{Fore.BLACK}{'-' * 145}\033[0m")

# Imprime o fundo com a altura desejada
[print(cor_de_fundo + ' ' * largura_da_linha) for _ in range(altura_do_fundo)]

# Texto que você quer em preto
texto = 'Modos de abertura em arquivos'

# Imprime o texto "Bloco with" em preto no meio do fundo amarelo
print(Fore.BLACK + cor_de_fundo + texto.center(largura_da_linha))

# Imprime o fundo novamente com a altura desejada
[print(cor_de_fundo + ' ' * largura_da_linha) for _ in range(altura_do_fundo)]

# Imprime as linhas de término com a cor amarela
print(f"{Fore.BLACK}{'-' * 145}\033[0m")

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

# arquivo = open('../../pythonProject/texto.txt', 'r', encoding='utf-8')

# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(Fore.CYAN + f"{'↓ Modos de abertura em arquivos ↓'.center(145)}\n"f"{Fore.CYAN}{'-' * 145}\033[0m\n")

print("r -> abre para leitura - padrão")
print("w -> abre para escrita - sobrescreve caso o arquivo já exista")
print("x -> abre para escrita - somente se o arquivo não existir. caso o arquivo exista, gera FileExistsError.")

print(Fore.GREEN + f'\ntry:\n'f'    with open("../../pythonProject/university.txt'', x'", encoding=utf-8) as arquivo:\n"
                   "        arquivo.write(Teste de conteúdo)\nexcept FileExistsError:\n    print(Arquivo já existe!')"
                   "\n")

try:
    with open('../../pythonProject/Python.txt', 'x', encoding='utf-8') as arquivo:
        arquivo.write('Teste escrevendo em arquivo\n')
except FileExistsError:
    print('Arquivo já existe!')
# print(arquivo.write)

# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------
