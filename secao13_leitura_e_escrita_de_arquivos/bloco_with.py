"""
Bloco with

O bloco with é utilizado para criar um contexto de trabalho, onde os recursos utilizados
são fechados após o bloco with.

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
largura_da_linha = 178

# Imprime as linhas de início com a cor amarela
print(f"{Fore.BLACK}{'-' * 178}\033[0m")

# Imprime o fundo com a altura desejada
[print(cor_de_fundo + ' ' * largura_da_linha) for _ in range(altura_do_fundo)]

# Texto que você quer em preto
texto = 'Bloco with'

# Imprime o texto "Bloco with" em preto no meio do fundo amarelo
print(Fore.BLACK + cor_de_fundo + texto.center(largura_da_linha))

# Imprime o fundo novamente com a altura desejada
[print(cor_de_fundo + ' ' * largura_da_linha) for _ in range(altura_do_fundo)]

# Imprime as linhas de término com a cor amarela
print(f"{Fore.BLACK}{'-' * 178}\033[0m")

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

# arquivo = open('../../pythonProject/texto.txt', 'r', encoding='utf-8')

print(Fore.CYAN + f"{'↓ Manipulando um arquivo com with ↓'.center(178)}\n"f"{Fore.CYAN}{'-' * 178}\033[0m\n")

print(Fore.WHITE + f'arquivo = open(../../pythonProject/texto.txt', 'r', 'encoding=utf-8\n')

#  forma Pythônica de se manipular arquivos
with open('../../pythonProject/texto.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.readlines())  # o with fecha a leitura do arquivo

print(Fore.BLUE + f'\nAo tentar imprimir novamente:\n\n' + Fore.RED + f'print(arquivo.read()\nValueError: I/O operation'
                                                                      f'on closed file.')
