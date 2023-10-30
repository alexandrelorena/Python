"""
Sistema de arquivos - manipulação


"""

from colorama import Fore, Back, init
import os
# import platform
# import sys
import shutil
from send2trash import send2trash
import tempfile

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
texto = 'Sistema de arquivos - manipulação'

# Imprime o texto "Bloco with" em preto no meio do fundo amarelo
print(Fore.BLACK + cor_de_fundo + texto.center(largura_da_linha))

# Imprime o fundo novamente com a altura desejada
[print(cor_de_fundo + ' ' * largura_da_linha) for _ in range(altura_do_fundo)]

# Imprime as linhas de término com a cor amarela
print(f"{Fore.BLACK}{'-' * 145}\033[0m")

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

print(Fore.CYAN + f"{'↓ Verificando se existe um arquivo ou diretório ↓'.center(145)}\n"f"{Fore.CYAN}{'-' * 145}\033[0m"
                  f"\n")

print(os.getcwd())

os.chdir('..')
print(os.getcwd())


item_arquivo = os.path.exists('arquivo.txt')
item_frutas = os.path.exists('frutas.txt')
item_geek = os.path.exists('geek')

print("Existe arquivo.txt?", end=' ')
if item_arquivo:
    print(Fore.BLUE + 'TRUE')
else:
    print(Fore.RED + 'FALSE')

print("Existe frutas.txt?", end=' ')
if item_frutas:
    print(Fore.BLUE + 'TRUE')
else:
    print(Fore.RED + 'FALSE')

print("Existe o diretório geek?", end=' ')
if item_geek:
    print(Fore.BLUE + 'TRUE')
else:
    print(Fore.RED + 'FALSE')

#  Paths relativos
print(os.path.exists('geek/university'))
print(os.path.exists('geek/university/../geek3.py'))
print(os.path.exists('geek/university/texto.txt'))

# Paths absolutos
print(os.path.exists('/home/pythonProject'))
print(os.path.exists('/Users/Usuario/pycharmProjects/pythonProject'))
print(os.path.exists('/Users/Usuario/pycharmProjects/pythonProject/texto.txt'))

# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ Criando um arquivo ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

open('arquivo-teste.txt', 'w').close()

open('arquivo-teste2.txt', 'a').close()

with open('arquivo-teste3.txt', 'w') as arquivo:
    pass  # pass indica que não tem mais nada no bloco

# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

# Especifica o caminho absoluto para o arquivo
caminho_absoluto = '/Users/Usuario/pycharmProjects/pythonProject/university2.txt'


print(Fore.LIGHTRED_EX + "try:\n    with " + Fore.MAGENTA + "open" + Fore.BLACK + "(caminho_absoluto, 'w'):\n"
      + Fore.LIGHTRED_EX + "        pass\n " + Fore.MAGENTA + "   print " + Fore.BLACK + "(" + Fore.GREEN + "Arquivo "
      + Fore.BLACK + "{caminho_absoluto} " + Fore.GREEN + "criado com ""sucesso.)""\n" + Fore.LIGHTRED_EX + "except "
      + Fore.MAGENTA + "OSError as e:\n " + Fore.MAGENTA + "   print" + Fore.BLACK + "("
      + Fore.GREEN + "Erro ao criar o arquivo:" + Fore.BLACK + "{e}')\n")

# Cria um arquivo vazio no caminho especificado
try:
    with open(caminho_absoluto, 'w'):
        pass
    print(Fore.LIGHTYELLOW_EX + "Arquivo " + Fore.BLACK + f'{caminho_absoluto}' + Fore.LIGHTYELLOW_EX +
          " criado com sucesso.")

except OSError as e:
    print(Fore.LIGHTRED_EX + f'Erro ao criar o arquivo: {e}')

# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ Criando um diretório ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

try:
    os.mkdir('templates2')
    print(Fore.LIGHTGREEN_EX + "Diretório criado com sucesso")
except FileExistsError:
    print(Fore.LIGHTRED_EX + "Diretório já existe")

#  criando diretórios UM POR VEZ!

try:
    os.mkdir('templates3')
    print(Fore.LIGHTGREEN_EX + "Diretório criado com sucesso")
except FileExistsError:
    print(Fore.LIGHTRED_EX + "Diretório já existe")

try:
    os.mkdir('templates3/geek')
    print(Fore.LIGHTGREEN_EX + "Diretório criado com sucesso")
except FileExistsError:
    print(Fore.LIGHTRED_EX + "Diretório já existe")

try:
    os.mkdir('templates3/geek/university')
    print(Fore.LIGHTGREEN_EX + "Diretório criado com sucesso")
except FileExistsError:
    print(Fore.LIGHTRED_EX + "Diretório já existe")

#  criando vários diretórios AO MESMO TEMPO!

try:
    os.makedirs('templates4/geek/university')
    print(Fore.LIGHTGREEN_EX + "Diretório criado com sucesso")
except FileExistsError:
    print(Fore.LIGHTRED_EX + "Diretório já existe")

os.makedirs('templates5/geek/university', exist_ok=True)  # parâmetro 'exist_ok=True' ignora erro se já existir.

# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ Renomeando um diretório ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")
try:
    os.rename('templates2', 'renomeado2')
    print(Fore.LIGHTGREEN_EX + "Diretório renomeado com sucesso")
except FileNotFoundError:
    print(Fore.LIGHTRED_EX + "Diretório não existe")
except FileExistsError:
    print(Fore.LIGHTRED_EX + "Diretório já existe")

try:
    os.rename('renomeado/university', 'renomeado3')
except PermissionError:
    print(Fore.LIGHTRED_EX + "Ação não permitida")
except FileNotFoundError:
    print(Fore.LIGHTRED_EX + "Diretório não existe")

# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ Renomeando um arquivo ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")
try:
    os.rename('renomeado/university/geek3.py', 'renomeado/university/teste.txt')  # tem que passar o caminho todo
    print(Fore.LIGHTGREEN_EX + "Arquivo renomeado com sucesso")
except FileNotFoundError:
    print(Fore.LIGHTRED_EX + "Arquivo não existe")

# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ Deletando arquivos e diretórios - OBS: não vão para lixeira ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

try:
    os.remove('renomeado/university/__init__.py')  # os.remove não remove diretórios. Apenas arquivos
    print(Fore.LIGHTGREEN_EX + "Arquivo deletado com sucesso")
except FileNotFoundError:
    print(Fore.LIGHTRED_EX + "Arquivo não existe")

#  removendo diretórios vazios

try:
    os.rmdir('templates6')
    print(Fore.LIGHTGREEN_EX + "Diretório excluído com sucesso")
except FileNotFoundError:
    print(Fore.LIGHTRED_EX + "Diretório não existe")
except OSError:
    print(Fore.LIGHTRED_EX + "O diretório não está vazio")

#  removendo todo o conteúdo de uma vez

for arquivo in os.scandir('templates4'):
    if arquivo.is_file():
        os.remove(arquivo.path)
    elif arquivo.is_dir():
        shutil.rmtree(arquivo.path)

diretorios_a_excluir = ['renomeado', 'renomeado2', 'templates2', 'templates3', 'templates4', 'templates5']

#  usando For

for diretorio in diretorios_a_excluir:
    if os.path.exists(diretorio):
        shutil.rmtree(diretorio)
        print(f"Diretório '{diretorio}' excluído com sucesso")
    else:
        print(f"O diretório '{diretorio}' não existe.")

#  usando removedirs()
try:
    os.removedirs('geek2/geek3/geek4')
except FileNotFoundError:
    print(Fore.LIGHTRED_EX + "Diretório não existe")

try:
    os.remove('frutas1.txt')
    print(Fore.LIGHTGREEN_EX + "Diretório excluído com sucesso")
except FileNotFoundError:
    print(Fore.LIGHTRED_EX + "Diretório não existe")

try:
    send2trash('frutas2.txt')
    print(Fore.LIGHTGREEN_EX + "Diretório excluído com sucesso")
except FileNotFoundError:
    print(Fore.LIGHTRED_EX + "Diretório não existe")


"""with open('cesta_de_frutas.txt', 'w', encoding='utf-8') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair!')
        if fruta != 'sair':  # precisa de tratamento ao digitar maisúsculas
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break"""

#  criando diretório_fornecido pelo usuário
diretorio_fornecido = input('Digite um nome para o diretório: ')

try:
    os.mkdir(diretorio_fornecido)
    print(Fore.LIGHTGREEN_EX + f'Diretório ' + Fore.BLUE + f'{diretorio_fornecido}' + Fore.BLACK + f' criado '
          + Fore.LIGHTGREEN_EX + f'com sucesso')
except FileExistsError:
    print(Fore.LIGHTGREEN_EX + f'Diretório ' + Fore.BLUE + f'{diretorio_fornecido}' + Fore.LIGHTGREEN_EX +
          f' já existe")')

#   send2trash -> enviando para lixeira o diretório_fornecido pelo usuário
try:
    send2trash(diretorio_fornecido)
    print(Fore.LIGHTGREEN_EX + "Diretório excluído com sucesso")
except FileNotFoundError:
    print(Fore.LIGHTRED_EX + "Diretório não existe")
# print(diretorio_fornecido)


#  excluindo diretório_fornecido pelo usuário
try:
    os.rmdir(diretorio_fornecido)
    print(Fore.LIGHTGREEN_EX + f'Diretório ' + Fore.BLUE + f'{diretorio_fornecido}' + Fore.RED + f' excluído '
          + Fore.LIGHTGREEN_EX + f'com sucesso')
except FileNotFoundError:
    print(Fore.LIGHTGREEN_EX + f'Diretório ' + Fore.BLUE + f'{diretorio_fornecido}' + Fore.LIGHTGREEN_EX +
          f' não existe')

# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ Trabalhando com diretórios e arquivos temmporários ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

#  criando diretório temporário
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()

#  criando arquivo temporário com bloco with

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')  # b converte para binário
    tmp.seek(0)
    print(tmp.read())
#  em arquivos temporários só conseguimos escrever bits => b''


#  criando arquivo temporário sem o bloco with
arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')  # b converte para binário
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')

print(arquivo.name)

print(arquivo.read())

input()

arquivo.close()
