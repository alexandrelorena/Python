"""
Sistema de arquivos e navegação

Para fazer uo de manipulação de arquivos do SO precisamos importar o módulo os.

os -> Operation System

"""

from colorama import Fore, Back, init
import os
import platform
# import sys

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
texto = 'Sistema de arquivos e navegação'

# Imprime o texto "Bloco with" em preto no meio do fundo amarelo
print(Fore.BLACK + cor_de_fundo + texto.center(largura_da_linha))

# Imprime o fundo novamente com a altura desejada
[print(cor_de_fundo + ' ' * largura_da_linha) for _ in range(altura_do_fundo)]

# Imprime as linhas de término com a cor amarela
print(f"{Fore.BLACK}{'-' * 145}\033[0m")

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

print(Fore.CYAN + f"{'↓ getcwd() ↓'.center(145)}\n"f"{Fore.CYAN}{'-' * 145}\033[0m\n")

print(Fore.MAGENTA + "getcwd() -> pega o current work directory e retorna o path (caminho) absoluto")

print(Fore.GREEN + "\nprint(os.getcwd())")

print(Fore.BLUE + f'\n{os.getcwd()}\n')


print(f"{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ chdir('..') ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(Fore.MAGENTA + "os.chdir('..') -> para voltar um diretório")

print(Fore.GREEN + "\nprint(os.getcwd())")

print(Fore.BLUE + f'\n{os.getcwd()}')

os.chdir('..')
print(os.getcwd())

os.chdir('..')
print(os.getcwd())

# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(Fore.MAGENTA + "\nos.chdir('..') -> checar se um diretório é absoluto " + Fore.GREEN + "(TRUE)" + Fore.MAGENTA +
      " ou relativo " + Fore.RED + "(FALSE)\n")

caminho = os.path.isabs("/Users/Usuario/PycharmProjects/pythonProject/secao13_leitura_e_escrita_de_arquivos/")
#  forma 1
print(Fore.BLACK + f'Forma 1: print(os.path.isabs()) =>', end=' ')

if caminho is True:
    print(Fore.BLUE + 'TRUE')
else:
    print(Fore.RED + 'FALSE')

#  forma 2
print(Fore.YELLOW + f'Forma 2: path = "/Users/Usuario/PycharmProjects/pythonProject/secao13_leitura_e_escrita_de_'
                    f'arquivos/"')
print(Fore.LIGHTYELLOW_EX + f'print(os.path.isabs(path)) =>', end=' ')

if caminho is True:
    print(Fore.BLUE + 'TRUE')
else:
    print(Fore.RED + 'FALSE')

print(Fore.RED + '\nNo Windows: ' + Fore.BLACK + 'print(os.path.isabs(r C:\\Users\\Usuario)) =>', end=' ')

diretorio = os.path.isabs(r'C:\Users\Usuario')  # r é usado para tratar a barra invertida na formatação.

if diretorio is True:
    print(Fore.BLUE + 'TRUE')
else:
    print(Fore.RED + 'FALSE')

# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ Identificando o Sistema Operacional ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

system_info = platform.uname()
print(Fore.YELLOW + "system_info = platform.uname()" + Fore.LIGHTYELLOW_EX)

field_names = ['system', 'node', 'release', 'version', 'machine', 'processor']
system_info_list = list(system_info)

for field_name, value in zip(field_names, system_info_list):
    print(f"{field_name}: {value}")

if platform.architecture()[0] == "32bit":
    print("O sistema é de 32 bits.")
elif platform.architecture()[0] == "64bit":
    print("O sistema é de 64 bits.")
else:
    print("A arquitetura do sistema não pôde ser determinada.")

# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ Criando/adicionando diretório oo caminho ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

print(Fore.YELLOW + "print(os.getcwd())\nres = os.path.join(os.getcwd(), 'workspace', 'sistema')\nos.chdir(res)\n\n"
                    "diretorio = input(Digite o nome do diretório a ser criado: )\ncaminho_atual = os.getcwd()"
                    "novo_caminho = os.path.join(caminho_atual, diretorio)\n\n"
                    "if not os.path.exists(novo_caminho):\n    os.makedirs(novo_caminho)\n\n"
                    "os.chdir(novo_caminho)\nprint(os.getcwd())\n" + Fore.LIGHTYELLOW_EX)

print(os.getcwd())
res = os.path.join(os.getcwd(), 'workspace', 'sistema')  # navegar acessando os diretórios
os.chdir(res)

"""# Obtém o nome do diretório a ser criado a partir do usuário
diretorio = input("Digite o nome do diretório a ser criado: ")

# Obtém o caminho atual
caminho_atual = os.getcwd()

# Junta o caminho atual com o nome do diretório "teste"
novo_caminho = os.path.join(caminho_atual, diretorio)

# Verifica se o diretório "teste" já existe
if not os.path.exists(novo_caminho):
    os.makedirs(novo_caminho)

# Muda o diretório de trabalho para o novo caminho
os.chdir(novo_caminho)

# Imprime o novo caminho de trabalho
print(os.getcwd())"""

# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ os.listdir() - Listando os diretórios ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

#  Forma 1 - na mesma linha

print(Fore.YELLOW + "os.listdir()\n" + Fore.LIGHTCYAN_EX + "Itens: " + Fore.LIGHTBLUE_EX + f'{os.listdir()}')
print()
print(Fore.YELLOW + "len(os.listdir()\n" + Fore.LIGHTCYAN_EX + "Quantidade: " + Fore.LIGHTBLUE_EX +
      f'{len(os.listdir())}')
print()
diretorio = 'C://'
print(Fore.YELLOW + "os.listdir(C:/)\n" + Fore.LIGHTCYAN_EX + "Conteúdo C://: " + Fore.LIGHTBLUE_EX +
      f'{os.listdir("C:/")}\n')


# Obtém a lista de arquivos e diretórios no diretório 'C://'
lista_de_arquivos = os.listdir(diretorio)

# Forma 2 - lista pulando linha
# Imprime a lista, pulando linha entre os itens
print(Fore.YELLOW + "conteúdo C:// - pulando linha \n" + Fore.LIGHTCYAN_EX + "for item in lista_de_arquivos:\n"
      + Fore.MAGENTA + "    print(Fore.LIGHTBLUE_EX + f'{item}')\n")
for item in lista_de_arquivos:
    print(Fore.LIGHTBLUE_EX + f'{item}')

# scandir()
print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ scandir() ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

print(f'diretório atual: ' + Fore.MAGENTA + os.getcwd())

scanner = os.scandir()
arquivos = list(scanner)

print(Fore.BLACK + f'\nUsando ' + Fore.LIGHTCYAN_EX + 'scandir() ' + Fore.BLACK + 'no diretório atual:\n'
      + Fore.MAGENTA + f'{arquivos}\n')

print(dir(arquivos[3].name))

print(Fore.CYAN + f'\ninode(): {arquivos[2].inode()}')
print(Fore.BLUE + f'is_dir(): {arquivos[2].is_dir()}')
print(Fore.YELLOW + f'is_file(): {arquivos[2].is_file()}')
print(Fore.LIGHTRED_EX + f'is_symlink(): {arquivos[2].is_symlink()}')
print(Fore.BLACK + f'name: {arquivos[2].name}')  # nome do arquivo
print(Fore.GREEN + f'path: {arquivos[2].path}')  # caminho até o arquivo
print(Fore.MAGENTA + f'stat(): {arquivos[2].stat()}')  # estatísticas

# É preciso fechar a função scandir() após usá-la

scanner.close()
