"""
Debuggando com PDB

PDB >> Python Debugger > A partir do Python 3.7, essa biblioteca não é mais
necessária importar pois foi incorporada como função built-in (integrada) chamada
breakpoint().

- comandos básicos:
# l >> listar onde estamos no código
# n >> próxima linha
# p >> imprime variável
# c >> continua a execução - finaliza o debugging


# Exemplo 1 - import pdb (no início do arquivo)

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)


# Exemplo 2 - import pdb; pdb.set_trace():

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()  # 2 comandos python na mesma linha, usa-se ';'
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

#  Este método de utilização do import pdb é feito apenas onde vamos debuggar, e não no início do arquivo, pois deverá
#  ser removido.


# Exemplo 3 - breakpoint():

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

"""
# import pdb

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

print(f'\n\033[37m-------------------------- ↓ \033[34mDebuggando com Debugger\033[37m ↓ -------------------------'
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

print(f'\n\033[37m--------------------------------- ↓ \033[34mExemplo 1\033[37m ↓ --------------------------------'
      f'\n\033[0m')

# Exemplo 1

# comandos básicos:
# l >> listar onde estamos no código
# n >> próxima linha
# p >> imprime variável
# c >> continua a execução - finaliza o debugging
"""nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)
"""

# Exemplo 2
print(f'\n\033[37m--------------------------------- ↓ \033[34mExemplo 2\033[37m ↓ --------------------------------'
      f'\n\033[0m')

# comandos básicos:

# l >> listar onde estamos no código
# n >> próxima linha
# p >> imprime variável
# c >> continua a execução - finaliza o debugging

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
# import pdb; pdb.set_trace()  # 2 comandos python na mesma linha, usa-se ';'
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

#  Este método de utilização do import pdb é feito apenas onde vamos debuggar, e não no início do arquivo, pois deverá
#  ser removido.


# Exemplo 3 - breakpoint()

print(f'\n\033[37m-------------------------- ↓ \033[34mExemplo 3 - breakpoint()\033[37m ↓ ------------------------'
      f'\n\033[0m')

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)
