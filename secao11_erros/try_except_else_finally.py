"""
Try / Except / Else /Finally

Quando tratar código??

TODA ENTRADA DEVE SER TRATADA!

OBS: A função do usuário é DESTRUIR seu sistema!

Exemplos:

    Try / Except / Else
        try:
            num = int(input('Informe um número: '))
        except ValueError:
            print("Valor incorreto")
        else:  # é executado somente se não ocorrer o erro.
            print(f'Você digitou {num}')

    Try / Except / Else / Finaly
        try:
             num = int(input('Informe um número: '))
        except ValueError:
            print('Você não digitou um valor válido.')
        else:
            print(f'Você digitou {num}')
        finally:  # o bloco finaly é SEMPRE executado. Geralmente utilizado para fechar ou desalocar recursos.
            print('Executando o finaly')

Exemplo complexo ERRADO:

        def dividir(a, b):
            return a / b

        try:
             num1 = int(input('Informe o primeiro número: '))
        except ValueError:
            print('O valor precisa ser numérico')
            num2 = int(input('Informe o segundo número: '))
        except ValueError:
            print('O valor precisa ser numérico')
        try:
            print(dividir(num1, num2))
        except NameError:
            print('Valor incorreto')

Exemplo complexo CORRETO:

        def dividir(a, b):
            try:
                return int(a) / int(b)
            except ValueError:
                return 'Valor incorreto'
            except ZeroDivisionError:
                return 'Não é possível dividir por zero'

        num1 = input('Informe o primeiro número: ')
        num2 = input('Informe o segundo número: ')
        print(dividir(num1, num2))

Exemplo SEMI-GENERICO:

        def dividir(a, b):
            try:
                return int(a) / int(b)
            except (ValueError, ZeroDivisionError) as err:
                return f'Ocorreu o problema: {err}'

        num1 = input('Informe o primeiro número: ')
        num2 = input('Informe o segundo número: ')
        print(dividir(num1, num2))

"""

print(f"\033[33m{'-' * 80}\n\033[94m{'↓ Try / Except / Else /Finally ↓'.center(80)}\033[33m\n{'-' * 80}"
      f"\033[0m\n")

# ---------------------------------------------- ↓ Try / Except / Else  ↓ --------------------------------------

print(f'\033[37m---------------------------- ↓ \033[34mTry / Except / Else\033[37m ↓ ---------------------------'
      f'\n\033[0m')

try:
    num = int(input('Informe um número: '))
except ValueError:
    print("Valor incorreto")
else:  # é executado somente se não ocorrer o erro.
    print(f'Você digitou {num}')

# ---------------------------------------------- ↓ Try / Except / Else / Finaly  ↓ -------------------------------------

print(f'\n\033[37m------------------------ ↓ \033[34mTry / Except / Else / Finaly\033[37m ↓ ----------------------'
      f'\n\033[0m')

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Você digitou {num}')
finally:  # o bloco finaly é SEMPRE executado. Geralmente utilizado para fechar ou desalocar recursos.
    print('Executando o finaly')

# ---------------------------------------------- ↓ exemplo complexo CORRETO  ↓ -------------------------------------

print(f'\n\033[37m-------------------------- ↓ \033[34mexemplo complexo CORRETO\033[37m ↓ -------------------------'
      f'\n\033[0m')


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível dividir por zero'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))

# ------------------------------------------ ↓ exemplo complexo - SEMI-GENÉRICO  ↓ ---------------------------------

print(f'\n\033[37m---------------------- ↓ \033[34mexemplo complexo - SEMI-GENÉRICO\033[37m ↓ ---------------------'
      f'\n\033[0m')


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu o problema: {err}'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))
