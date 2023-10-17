"""
Levantando os próprios erros com raise

raise -> Lança exceções

- É uma palavra reservada

sintaxe: TipoDoErro('Mensagem de erro')

exemplos:

    a) raise ValueError('Valor incorreto')

    b) def colore(texto, cor):
        if type(texto) is not str:
            raise TypeError('Texto precisa ser uma string')
        if type(cor) is not str:
            raise TypeError('cor precisa ser uma string')
        print(f'O texto {texto} será impresso na cor {cor}')

    colore('Geek', 4)

    c) def colore(texto, cor):
        if type(texto) is not str:
           raise TypeError('Texto precisa ser uma string')
        if type(cor) is not str:
           raise TypeError('cor precisa ser uma string')
       print(f'O texto {texto} será impresso na cor {cor}')

    colore(True, 'azul')


"""

print(f"\033[33m{'-' * 80}\n\033[94m{'↓ Levantando os próprios erros com raise ↓'.center(80)}\033[33m\n{'-' * 80}"
      f"\033[0m\n")

# ------------------------------------------ ↓ Usando o raise - ex 1 ValueError ↓ --------------------------------------

print(f'\033[37m--------------------- ↓ \033[34mUsando o raise - ex 1 ValueError\033[37m ↓ ---------------------'
      f'\n\033[0m')

print("raise ValueError('Valor incorreto')")

print("\n\033[31mTraceback (most recent call last):\nFile 'C:/Users/Usuario/PycharmProjects/pythonProject/secao11_erros"
      "/raise.py', line 25, in <module>\nraise ValueError('Valor incorreto')\nValueError: Valor incorreto\n")

# ------------------------------------------ ↓ Usando o raise - ex 2 TypeError ↓ --------------------------------------

print(f'\033[37m--------------------- ↓ \033[34mUsando o raise - ex 2 TypeError\033[37m ↓ ----------------------'
      f'\n\033[0m')

print("def colore(texto, cor):\nif type(texto) is not str:\nraise TypeError('Texto precisa ser uma string')\n"
      "if type(cor) is not str:\nraise TypeError('cor precisa ser uma string')\nprint(f'O texto {texto} será impresso "
      "na cor {cor}')\ncolore('Geek', 4)")

print("\n\033[31mTraceback (most recent call last):\nFile 'C:/Users/Usuario/PycharmProjects/pythonProject/secao11_erros"
      "/raise.py', line 55, in <module>\ncolore('Geek', 4)\nFile 'C:/Users/Usuario/PycharmProjects/pythonProject/secao"
      "11_erros/raise.py', line 51, in colore raise \nTypeError('cor precisa ser uma string')\nTypeError: cor precisa "
      "ser uma string")


"""def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')


colore(True, 'azul')


OBS: O raise, assim como o return, finaliza a função. Nada após o raise é executado.

"""
# ------------------------------------ ↓ Usando o raise - ex 3 TypeError + ValueError ↓ --------------------------------

print(f'\033[37m--------------- ↓ \033[34mUsando o raise - ex 3 TypeError + ValueError\033[37m ↓ ---------------'
      f'\n\033[0m')


print("def colore(texto, cor):\ncores = ('verde', 'amarelo', 'azul', 'branco')\nif type(texto) is not str:\nraise "
      "TypeError('Texto precisa ser uma string')\nif type(cor) is not str:\nraise TypeError('cor precisa ser uma string"
      "')\nif cor not in cores:\nraise ValueError(f'A cor precisa ser uma entre: {cores}')\nprint(f'O texto {texto} "
      "será impresso na cor {cor}')\ncolore('Geek', 'vermelho')")

print("\n\033[31mTraceback (most recent call last):\nFile 'C:/Users/Usuario/PycharmProjects/pythonProject/secao11_erros"
      "/raise.py', line 55, in <module>\ncolore('Geek', 'vermelho')\nFile 'C:/Users/Usuario/PycharmProjects/python"
      "Project/secao11_erros/raise.py', line 51, in colore \nraise ValueError(f'A cor precisa ser uma entre: {cores}')"
      "\nValueError: A cor precisa ser uma entre: ('verde', 'amarelo', 'azul', 'branco')")


"""def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek', 'vermelho')"""

# ------------------------------------ ↓ Usando o raise - ex 4 TypeError + ValueError ↓ --------------------------------

print(f'\033[37m--------------- ↓ \033[34mUsando o raise - ex 4 TypeError + ValueError\033[37m ↓ ---------------'
      f'\n\033[0m')
