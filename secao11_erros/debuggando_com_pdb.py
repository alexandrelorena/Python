"""
Debuggando com PDB

PDB >> Python Debugger

"""
import pdb

print(f"\033[33m{'-' * 80}\n\033[94m{'↓ Debuggando com PDB ↓'.center(80)}\033[33m\n{'-' * 80}"
      f"\033[0m\n")

# ---------------------------------------------- ↓ Debuggando com PDB ↓ --------------------------------------

# prática ruim >> print para debuggar


def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu o problema: {err}'


print(dividir(4, 7))

# ---------------------------------------------- ↓ Debuggando com Debugger ↓ --------------------------------------

print(f'\033[37m-------------------------- ↓ \033[34mDebuggando com Debugger\033[37m ↓ -------------------------'
      f'\n\033[0m')

# exemplo com Pycharm >> Utilizando breakpoints e depois cicar no 'inseto' ao lado do run.


def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu o problema: {err}'


print(dividir(4, 7))

# exemplo com Python Debugger >> importar a bibioteca pdb >> função set_trace()

# comandos básicos:
# l >> listar onde estamos no código
# n >> próxima linha
# p >> imprime variável
# c >> continua a execução - finaliza o debugging
nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)