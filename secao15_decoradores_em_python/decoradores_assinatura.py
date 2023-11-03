from colorama import Fore, Back, init
# from random import choice
from secao08_funcoes.minhas_funcoes import imprimir_com_cores
"""
Decorators com diferentes assinaturas.

A assinatura de uma função compõe em seu retorno: o nome e o parâmetro de entrada.
- padrão de projeto : Decorator Pattern

"""
# -------------------------------------------- ↓ Bloco título ↓ --------------------------------------------

# Inicialize o Colorama

init(autoreset=True)

# Cor de fundo que você deseja
cor_de_fundo = Back.BLUE

# Altura do fundo (número de linhas)
altura_do_fundo = 1

# Largura da linha
largura_da_linha = 145

# Imprime as linhas de início com a cor escolhida
print(f"{Fore.BLACK}{'-' * 145}\033[0m")

# Imprime o fundo com a altura desejada
[print(cor_de_fundo + ' ' * largura_da_linha) for _ in range(altura_do_fundo)]

# Texto que você quer em preto
texto = 'Decorators com diferentes assinaturas'

# Imprime o texto "Bloco with" em preto no meio do fundo amarelo
print(Fore.BLACK + cor_de_fundo + texto.center(largura_da_linha))

# Imprime o fundo novamente com a altura desejada
[print(cor_de_fundo + ' ' * largura_da_linha) for _ in range(altura_do_fundo)]

# Imprime as linhas de término com a cor escolhida
print(f"{Fore.BLACK}{'-' * 145}\033[0m")

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

print(Fore.BLUE + f"↓ Decorators com funções (Síntaxe não recomendada) ↓".center(145) + f"\n{Fore.CYAN}{'-' * 145}"
                                                                                        f"\033[0m\n")

print(Fore.MAGENTA + "def seja_educado(funcao):\n    def sendo():\n        print('Foi um prazer conhecer você!')\n"
                     "        funcao()\n        print('Tenha um ótimo dia!')\n\n    return sendo\n\n")


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'


print(saudacao('Felicity'))

print(ordenar('Picanha', 'Batata frita'))


print(Fore.YELLOW + "def saudacao():\n    print('Seja bem-vindo(a) à Geek University')\n")

@gritar
def lol():
    return 'lol'