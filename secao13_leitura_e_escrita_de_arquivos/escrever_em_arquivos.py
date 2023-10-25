"""
Escrevendo em arquivos

Ao abrir um aruivo para leitura, não podemos escrever nele.

Ao abrir um arquivo para escrita, não podemos lê-lo.

O arquivo é criado ao abrir paa escrita com 'write'.

Esta função recebe uma string como parâmetro.

O texto é sobrescrito. O que tinha antes, é substituído.

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
texto = 'Escrevendo em arquivos'

# Imprime o texto "Bloco with" em preto no meio do fundo amarelo
print(Fore.BLACK + cor_de_fundo + texto.center(largura_da_linha))

# Imprime o fundo novamente com a altura desejada
[print(cor_de_fundo + ' ' * largura_da_linha) for _ in range(altura_do_fundo)]

# Imprime as linhas de término com a cor amarela
print(f"{Fore.BLACK}{'-' * 145}\033[0m")

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

# arquivo = open('../../pythonProject/texto.txt', 'r', encoding='utf-8')

print(Fore.CYAN + f"{'↓ Escrevendo em arquivos - forma Pythônica ↓'.center(145)}\n"f"{Fore.CYAN}{'-' * 145}\033[0m\n")

print(Fore.WHITE + f'with open(../../pythonProject/novo.txt', 'w', 'as arquivo\narquivo.write("Novos dados")\n'
                                                                   'arquivo.write("outros dados") \n')

with open('../../pythonProject/novo.txt', 'w') as arquivo:  # 'w' -> write -> modo para escrita
    arquivo.write('Novos dados\n')
    arquivo.write('outros dados\n')

print(arquivo.write)

print(Fore.MAGENTA + f"\n{Fore.MAGENTA}{'-' * 145}\n{'↓ Escrevendo em arquivos - forma Não Pythônica ↓'.center(145)}\n"
                     f""f"{Fore.MAGENTA}{'-' * 145}\033[0m"f"\n")

print(Fore.WHITE + f'arquivo = open(../../pythonProject/mais.txt', 'w', 'as arquivo\narquivo.write("Um texto qualquer")\narquivo.write("outros dados") \n')

arquivo = open('../../pythonProject/mais.txt', 'w')
arquivo.write('Um texto qualquer.\n')
arquivo.write('')
