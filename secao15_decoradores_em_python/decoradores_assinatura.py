from colorama import Fore, Back, init
from secao08_funcoes.minhas_funcoes import imprimir_com_cores
from termcolor import colored

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

print(Fore.BLUE + f"↓ Assinaturas ↓".center(145) + f"\n{Fore.CYAN}{'-' * 145}"f"\033[0m\n")

print(Fore.MAGENTA + "def gritar(funcao):\n    def aumentar(*args, **kwargs):\n        return funcao(*args, **kwargs)."
                     "upper()\n    return aumentar\n\n")

print(Fore.YELLOW + "@gritar\ndef saudacao(nome):\n    return Olá,"" eu sou o/a {nome}\n")

print(Fore.BLUE + "@gritar\ndef ordenar(principal, acompanhamento):\n    return f'Olá, eu gostaria de {principal}, "
                  "acompanhado de {acompanhamento}, por favor.'\n")

print(Fore.CYAN + "print(saudacao('Felicity'))\n")

print(Fore.LIGHTMAGENTA_EX + "print(ordenar('Picanha', 'Batata frita'))\n")


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}\n'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.\n'


print(Fore.YELLOW + saudacao('Felicity'))

print(Fore.LIGHTRED_EX + ordenar('Picanha', 'Batata frita'))

print(f"{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ Utilizando parâmetros nomeados' ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

print(Fore.BLUE + "print(ordenar(acompanhamento='Batata frita', principal='Picanha'))\n")

print(ordenar(acompanhamento='Batata frita', principal='Picanha'))

# ---------------------------------------------------------------------------------------------------------------------

print(f"{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ Decorators importando função 'imprimir_com_cores' ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

print(Fore.BLUE + "@gritar\ndef lol():\n    return 'lol'\n")

print(Fore.CYAN + "print(lol())\n")

print(Fore.YELLOW + "texto_colorido = lol()" + Fore.WHITE + "  # Obter o texto colorido\n")

print(Fore.LIGHTBLUE_EX + "imprimir_com_cores(texto_colorido)" + Fore.WHITE + "  # Imprimir o texto colorido\n")


@gritar
def lol():
    return 'lol'


texto_colorido = lol()  # Obter o texto colorido
imprimir_com_cores(texto_colorido)  # Imprimir o texto colorido

# ---------------------------------------------------------------------------------------------------------------------

print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ Decorators com função 'colorindo' ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")


print(Fore.BLUE + "def colorindo(text_color):\n    print(text_color)\n\n" + Fore.GREEN + "def gritar(funcao):\n    def "
                  "aumentar_e_colorir""(*args, **kwargs):\n        resultado = funcao(*args, **kwargs)\n        "
                  "resultado_aumentado = ""resultado.upper()\n        text_color = colored(resultado_aumentado, 'red')"
                  "\n        colorindo""(text_color)\n        return resultado_aumentado\n    return aumentar_e_colorir"
                  "\n\n" + Fore.MAGENTA + "@gritar\n""def lol():\n    return 'lol'\n\n" + Fore.WHITE + "# Chame a "
                  "função decorada\n" + Fore.BLACK + "lol()")


def colorindo(text_color):
    print(text_color)


# Defina o decorator @gritar
def gritar(funcao):
    def aumentar_e_colorir(*args, **kwargs):
        resultado = funcao(*args, **kwargs)
        resultado_aumentado = resultado.upper()
        text_color = colored(resultado_aumentado, 'red')
        colorindo(text_color)
        return resultado_aumentado
    return aumentar_e_colorir


# Use o decorator @gritar
@gritar
def lol():
    return 'lol'


print()
# Chame a função decorada
lol()

# ---------------------------------------------------------------------------------------------------------------------

print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ Decorators com argumentos ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

print(Fore.BLUE + "def verifica_primeiro_argumento(valor):\n    def interna(funcao):\n        def outra(*args, **kwargs"
                  "):\n            if args and args[0] != valor:\n                return f'Valor incorreto! Primeiro "
                  "argumento precisa ser {valor}'\n            return funcao(*args, **kwargs)\n        return outra\n"
                  "    return interna\n\n")

print(Fore.MAGENTA + "@verifica_primeiro_argumento(10)\ndef soma_dez(num1, num2):\n    return num1 + num2\n\n")


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return Fore.RED + f'Valor incorreto!' + Fore.BLUE + f' Primeiro argumento precisa ser' + Fore.YELLOW + \
                       f' {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


print(Fore.CYAN + "print(soma_dez(10, 12))\n")
print(soma_dez(10, 12))
print()
print(Fore.CYAN + "print(soma_dez(1, 21))\n")
print(soma_dez(1, 21))

print('\n----------------------------------------------------------------\n')

print(Fore.YELLOW + "@verifica_primeiro_argumento('pizza')\ndef comida_favorita(*args):\n    return args\n")


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    return args


print(Fore.CYAN + "print(comida_favorita('pizza', 'macarrão'))\n")
print(comida_favorita('pizza', 'macarrão'))
print()
print(Fore.CYAN + "print(comida_favorita('lazanha', 'pizza'))\n")
print(comida_favorita('lazanha', 'pizza'))
