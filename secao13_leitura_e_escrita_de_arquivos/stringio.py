"""
StringIO

- Permissão de Leitura
- Permissão de Escrita

StringIO -> Utilizado para ler e criar arquivos em memória.

"""

from colorama import Fore, Back, init
from io import StringIO

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
texto = 'StringIO'

# Imprime o texto "Bloco with" em preto no meio do fundo amarelo
print(Fore.BLACK + cor_de_fundo + texto.center(largura_da_linha))

# Imprime o fundo novamente com a altura desejada
[print(cor_de_fundo + ' ' * largura_da_linha) for _ in range(altura_do_fundo)]

# Imprime as linhas de término com a cor amarela
print(f"{Fore.BLACK}{'-' * 145}\033[0m")

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------
# StringIO -> ler e criar arquivos em memória
# -------------------------------------------- ↓ ------------ ↓ --------------------------------------------

print(Fore.CYAN + f"{'↓ StringIO -> ler e criar arquivos em memória ↓'.center(145)}\n"f"{Fore.CYAN}{'-' * 145}\033[0m"
                  f"\n")

print("- Permissão de Leitura")
print("- Permissão de Escrita")

print(Fore.GREEN + "\nmensagem = Este é apenas uma string normal, que foi criado e alocada na memória!\n"
                   "arquivo = StringIO(mensagem)\n"
                   "print(arquivo.read())\n")

mensagem = 'Este é apenas uma string normal, que foi criado e alocada na memória!'

arquivo = StringIO(mensagem)

print(arquivo.read())

arquivo.write('\nOutro texto')

arquivo.seek(0)

print(arquivo.read())
