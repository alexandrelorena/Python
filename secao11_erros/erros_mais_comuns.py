"""
Erros mais comuns em Python

1 - SyntaxError

      a)  def funcao:

      b) None = 1
             ^
            SyntaxError: cannot assign to None

      c) return

2 - NameError

      a) print(geek)

      b) geek()

3 - TypeError

      a) print(len(5))


4 - IndexError

      a) lista = ['Geek']
       print(lista[2])

      b) lista = ['Geek']
       print(lista[0][10])

5 - ValueError

      print(int('Geek'))

6 - KeyError
      dic = {'python': 'university'}
      print(dic['geek'])

7 - AttributeError

      tupla = {11, 2, 31, 4}
      print(tupla.sort())

8 - IndentationError

      a) def nova():
         print('Geek')
      b) for i in range(10):
         i + 1
         print(i)

OBS: Exceptions e Erros são sinônimos na programação.
"""

print(f"\033[33m{'-' * 80}\n\033[94m{'↓ Erros mais comuns em Python ↓'.center(80)}\033[33m\n{'-' * 80}\033[0m\n")

# ----------------------------------------------- ↓ SyntaxError ↓ --------------------------------------------

print(f'\033[37m-------------------------------- ↓ \033[34mSyntaxError \033[37m↓ ----------------------------'
      f'---\n\033[0m')

print("\033[35mErro de sintaxe. Algo que o Python não reconhece como parte da linguagem.\033[0m\n")


print("a) def funcao:  \nb) None = 1  \nc) return")

print("\n\033[31mTraceback (most recent call last): \nFile 'C:/Users/Usuario/PycharmProjects/pythonProject/secao11_"
      "erros/erros_mais_comuns.py', line 83 \ndef funcao: \n^SyntaxError: invalid syntax")

# ------------------------------------------------ ↓ NameError ↓ ---------------------------------------------

print(f'\n\033[37m-------------------------------- ↓ \033[34mNameError \033[37m↓ ----------------------------'
      f'---\n\033[0m')

print("\033[35mUma variável ou função não foi definida.\033[0m\n")

print("a) print(geek)  \nb) geek() ")

print("\n\033[31mTraceback (most recent call last):   \nFile 'C:/Users/Usuario/PycharmProjects/pythonProject/secao11_"
      "erros/erros_mais_comuns.py', line 88, in <module>  \nprint(geek) \nNameError: name 'geek' is not defined")

# ------------------------------------------------ ↓ TypeError ↓ ---------------------------------------------

print(f'\n\033[37m-------------------------------- ↓ \033[34mTypeError \033[37m↓ ----------------------------'
      f'---\n\033[0m')

print("\033[35mFunção/operação aplicada a um tipo errado.\033[0m\n")

print("print(len(5))")

print("\n\033[31mTraceback (most recent call last):   \nFile 'C:/Users/Usuario/PycharmProjects/pythonProject/secao11_"
      "erros/erros_mais_comuns.py', line 91, in <module> \nprint(len(5)) \nTypeError: object of type 'int' has no len()"
      )

# ------------------------------------------------ ↓ IndexError ↓ --------------------------------------------

print(f'\n\033[37m------------------------------- ↓\033[34m IndexError \033[37m↓ ----------------------------'
      f'---\n\033[0m')

print("\033[35mTentar acessar um elemento utilizando um índice inválido.\033[0m\n")

print("lista = ['Geek'] \nprint(lista[2])\n ")

print("\033[31mTraceback (most recent call last): \nFile 'C:/Users/Usuario/PycharmProjects/pythonProject/secao11_erros/"
      "erros_mais_comuns.py', line 92, in <module> \nprint(lista[2]) \nIndexError: list index out of range")

# ------------------------------------------------ ↓ ValueError ↓ --------------------------------------------

print(f'\n\033[37m------------------------------- ↓\033[34m ValueError \033[37m↓ ----------------------------'
      f'---\n\033[0m')

print("\033[35mFunção/operação built-in (integrada) recebe um argumento com tipo correto mas valor inapropriado.\033[0m"
      "\n")

print("print(int('Geek'))")

print("\n\033[31mTraceback (most recent call last): \nFile 'C:/Users/Usuario/PycharmProjects/pythonProject/secao11_"
      "erros/erros_mais_comuns.py', line 102, in <module> \nprint(int('Geek')) \nValueError: invalid literal for int() "
      "with base 10: 'Geek'")

# ------------------------------------------------ ↓ KeyError ↓ --------------------------------------------

print(f'\n\033[37m------------------------------- ↓\033[34m KeyError \033[37m↓ ----------------------------'
      f'---\n\033[0m')

print("\033[35mTentar acessar um dicionário com uma chave que não existe.\033[0m\n")

print("dic = {'python': 'university'} \nprint(dic['geek'])")

print("\n\033[31mTraceback (most recent call last): \nFile 'C:/Users/Usuario/PycharmProjects/pythonProject/secao11_"
      "erros/erros_mais_comuns.py', line 124, in <module> \nprint(dic['geek']) \nKeyError: 'geek'")

# ------------------------------------------------ ↓ AttributeError ↓ --------------------------------------------

print(f'\n\033[37m------------------------------- ↓\033[34m AttributeError \033[37m↓ ----------------------------'
      f'---\n\033[0m')

print("\033[35mUma variavel não tem um atributo/função.\033[0m\n")

print("tupla = {11, 2, 31, 4}\nprint(tupla.sort())")

print("\n\033[31mTraceback (most recent call last): \nFile 'C:/Users/Usuario/PycharmProjects/pythonProject/secao11_"
      "erros/erros_mais_comuns.py', line 137, in <module>\nprint(tupla.sort()) \nAttributeError: 'set' object has no "
      "attribute 'sort'")

# ------------------------------------------------ ↓ IndentationError ↓ --------------------------------------------

print(f'\n\033[37m------------------------------- ↓\033[34m IndentationError \033[37m↓ ----------------------------'
      f'---\n\033[0m')

print("\033[35mNão respeitamos a identação do Python (4 espaços).\033[0m\n")

print("def nova(): \nprint('Geek')")

print("\n\033[31mFile 'C:/Users/Usuario/PycharmProjects/pythonProject/secao11_erros/erros_mais_comuns.py', line 163 "
      "\nprint('Geek') \n^ IndentationError: expected an indented block")
