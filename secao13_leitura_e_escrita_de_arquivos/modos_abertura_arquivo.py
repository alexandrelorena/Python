"""
Modos de abertura em arquivos

r -> abre para leitura - padrão
w -> abre para escrita - sobrescreve caso o arquivo já exista
x -> abre para escrita - somente se o arquivo não existir. caso o arquivo exista, gera FileExistsError.
a -> Abre para escrita, adicionando o conteúdo ao final do arquivo se o arquivo já existir.
Senão, o arquivo será criado.
-

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
# Modos de abertura em arquivos
# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(Fore.CYAN + f"{'↓ Modos de abertura em arquivos ↓'.center(145)}\n"f"{Fore.CYAN}{'-' * 145}\033[0m\n")

print("r -> abre para leitura - padrão")
print("w -> abre para escrita - sobrescreve caso o arquivo já exista")
print("x -> abre para escrita - somente se o arquivo não existir. caso o arquivo exista, gera FileExistsError.")

print(Fore.GREEN + f'\ntry:\n'f'    with open("../../pythonProject/university.txt'', x'", encoding=utf-8) as arquivo:\n"
                   "arquivo.write(Teste escrevendo em arquivo)\nexcept FileExistsError:\n    print(Arquivo já existe!')"
                   "\n")

try:
    with open('../../pythonProject/Python.txt', 'x', encoding='utf-8') as arquivo:
        arquivo.write('Teste escrevendo em arquivo\n')
except FileExistsError:
    print('Arquivo já existe!')

# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(f"{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ a -> Abre para escrita, adicionando o conteúdo ao final do arquivo se o arquivo já existir. "
      f"Senão, o arquivo será criado. ↓".center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

print(Fore.GREEN + "with open('frutas.txt', 'a',  encoding='utf-8') as arquivo:\n"
                   "    while True:\n"
                   "        fruta = input('Informe uma fruta ou digite sair!')\n"
                   "        if fruta != 'sair':\n"
                   "            arquivo.write(fruta)\n"
                   "            arquivo.write(/n)\n"
                   "        else:\n"
                   "            break""\n")

with open('frutas.txt', 'a', encoding='utf-8') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair!')
        if fruta != 'sair':  # precisa de tratamento ao digitar maisúsculas
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(f"{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ a -> Adicionando o conteúdo no início do arquivo se ele já existir. ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

print(Fore.GREEN + "with open('../../pythonProject/novo.txt', 'r+', encoding='utf-8') as arquivo:\n"
                   "    arquivo.write('2/n')\n"
                   "    arquivo.write('1/n')\n"
                   "    arquivo.write(viiishe/n')\n"
                   "    arquivo.write('/n')\n"
                   "    arquivo.write('eiiiiita/n')\n"
                   "    arquivo.write('/n')\n"
                   "    arquivo.write('testando/n')\n"  # arquivo.seek(11)
                   "    arquivo.write('novamente/n')\n")
# arquivo.write('3\n')

with open('../../pythonProject/novo.txt', 'r+', encoding='utf-8') as arquivo:
    arquivo.write('2\n')
    arquivo.write('1\n')
    arquivo.write('viiishe\n')
    arquivo.write('\n')
    arquivo.write('eiiiiita\n')
    arquivo.write('\n')
    arquivo.write('testando"\n')
    # arquivo.seek(11)
    arquivo.write('novamente\n')
    # arquivo.write('3\n')
