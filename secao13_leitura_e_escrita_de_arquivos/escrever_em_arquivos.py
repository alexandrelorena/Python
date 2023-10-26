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

# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(Fore.CYAN + f"{'↓ Escrevendo em arquivos - forma Pythônica ↓'.center(145)}\n"f"{Fore.CYAN}{'-' * 145}\033[0m\n")

print(Fore.GREEN + f'with open(../../pythonProject/novo.txt' ', w' ', encoding=utf-8 as arquivo\n' + Fore.LIGHTBLUE_EX +
      'arquivo.write("Novos dados")\n' + Fore.LIGHTRED_EX + 'arquivo.write("outros dados") \n')

with open('../../pythonProject/novo.txt', 'w', encoding='utf-8') as arquivo:  # 'w' -> write -> modo para escrita
    arquivo.write('Novos dados\n')
    arquivo.write('outros dados\n')

# print(arquivo.write)

# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(Fore.BLUE + f'with open(../../pythonProject/geek.txt' ', w' ', encoding=utf-8) '
                  'as arquivo:\n' + Fore.BLACK + 'arquivo.write("Geek / n * 1000")\n')

with open('../../pythonProject/geek.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Geek\n' * 1000)

# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(Fore.MAGENTA + f"{Fore.YELLOW}{'-' * 145}\n{'↓ Escrevendo em arquivos - Pythônica com Loop ↓'.center(145)}\n"
                     f""f""f"{Fore.YELLOW}{'-' * 145}\033[0m"f"\n")

with open('frutas.txt', 'w', encoding='utf-8') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair!')
        if fruta != 'sair':  # precisa de tratamento ao digitar maisúsculas
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(Fore.MAGENTA + f"\n{Fore.MAGENTA}{'-' * 145}\n{'↓ Escrevendo em arquivos - forma Não Pythônica ↓'.center(145)}\n"
                     f""f"{Fore.MAGENTA}{'-' * 145}\033[0m"f"\n")

arquivo = open('../../pythonProject/mais.txt', 'w', encoding='utf-8')
arquivo.write('Um texto qualquer\n')  # é preciso pular linha para escrever o outro texto.
arquivo.write("Mais um texto")
print(Fore.CYAN + f'arquivo = open(../../pythonProject/mais.txt'', w, encoding=utf-8)\n' + Fore.BLACK +
      'arquivo.write("Um texto qualquer")')
arquivo.close()
