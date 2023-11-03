from colorama import Fore, Back, init
# from random import choice
# from secao08_funcoes.minhas_funcoes import imprimir_com_cores
"""
Decorators (decoradores)

- Decorators são funções
- Envolvem outras funções e aprimoram seus comportamentos
- São exemplos de HOF (Higher Order Functions)
- Tem sintaxe própria, usando "@" (Syntaxe sugar / açúcar sintatico)

/-----------------------------------/
/        Function Decorator         /
/-----------------------------------/

------------------------------------
//---------------------------------//
//         Função decorada         //
//---------------------------------//
//---------------------------------//


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
texto = 'Decorators'

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


def seja_educado(funcao):
    def sendo():
        print("Foi um prazer conhecer você!")
        funcao()
        print("Tenha um ótimo dia!")

    return sendo

#  Testando 1


print(Fore.YELLOW + "def saudacao():\n    print('Seja bem-vindo(a) à Geek University')\n")


def saudacao():
    print("Seja bem-vindo(a) à Geek University")


# saudacao()

teste = seja_educado(saudacao)
teste()
print()
#  Testando 2

print(Fore.BLUE + "def raiva():\n    print('EU TE ODEIO!')\n")


def raiva():
    print("EU TE ODEIO!")


raiva_educada = seja_educado(raiva)

raiva_educada()

# ---------------------------------------------------------------------------------------------------------------------

print(f"\n{Fore.CYAN}{'-' * 145}\033[0m\n" +
      f"{Fore.CYAN} ↓ Decorators com Syntax Sugar ↓"
      .center(145) + f"\n{Fore.CYAN}{'-' * 145}\033[0m\n")

print(Fore.MAGENTA + "def seja_educado_mesmo(funcao):\n    def sendo_mesmo():\n        print('Foi um prazer conhecer "
                     "você!')\n        funcao()\n        print('Tenha um excelente dia!')\n    return sendo_mesmo")


def seja_educado_mesmo(funcao):  # decorator function
    def sendo_mesmo():
        print("Foi um prazer conhecer você!")
        funcao()
        print("Tenha um excelente dia!")
    return sendo_mesmo


print()
print(Fore.YELLOW + "@seja_educado_mesmo\ndef apresentando():\n    print('Meu nome é Pedro')\n\napresentando()")


@seja_educado_mesmo  # decorator
def apresentando():
    print("Meu nome é Pedro")


print()
apresentando()

# ---------------------------------------------------------------------------------------------------------------------

print()

print(Fore.YELLOW + "@seja_educado_mesmo\ndef dormir():\n    print('Quero dormir...')""\n\ndormir()")


@seja_educado_mesmo
def dormir():
    print("Quero dormir...")


print()
dormir()

# ---------------------------------------------------------------------------------------------------------------------
