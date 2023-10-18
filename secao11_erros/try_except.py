"""
O bloco try / except

- Para tratamento de erros.

Sintaxe:

    try:
        //execução problemática
    except:
        //o que deve ser feito em caso de erro

Exemplos:

    a)  try:
            geek()
        except:
            print("Deu algum problema")

    b)  try:
            len(5)
        except:
            print("Deu algum problema")

OBS: Tratar erros de forma genérica não é a melhor opção. O ideal é SEMPRE
tratar de forma específica.

Tratando de forma correta:

    a)  try:
            geek()
        except NameError:
            print("Deu algum problema")

    b)  try:
            len(5)
        except TypeError:
            print("Deu algum problema")

"""

print(f"\033[33m{'-' * 80}\n\033[94m{'↓ Try / Except ↓'.center(80)}\033[33m\n{'-' * 80}"
      f"\033[0m\n")

# ---------------------------------------------- ↓ try/except - exemplo 1 ↓ --------------------------------------

print(f'\033[37m-------------------------- ↓ \033[34mtry/except - exemplo 1\033[37m ↓ --------------------------'
      f'\n\033[0m')

print(f'try: \n    geek() \nexcept: \n    print("Deu algum problema")\n')

# ------------------------------------------ ↓ try/except - exemplo 2 ↓ --------------------------------------

print(f'\033[37m-------------------------- ↓ \033[34mtry/except - exemplo 2\033[37m ↓ --------------------------'
      f'\n\033[0m')

print(f'try: \n    len(5) \nexcept: \n    print("Deu algum problema")\n')

# ------------------------------------------ ↓ try/except - exemplo 3 ↓ --------------------------------------

print(f'\033[37m-------------------------- ↓ \033[34mtry/except - exemplo 3\033[37m ↓ --------------------------'
      f'\n\033[0m')

print(f'try: \n    geek() \n\033[31mexcept NameError:\033[0m \n    print("Você está utilizando uma função inexistente!"'
      f')\n')

print(f'try: \n    len(5) \n\033[31mexcept TypeError: \033[0m \n    print("Você está utilizando uma função inexistente!'
      f'")\n')

print(f'try: \n    len(5) \n\033[31mexcept TypeError: \033[0m \n    print("Você está utilizando uma função inexistente!'
      f'")\n')

# ------------------------------------------ ↓ try/except - exemplo 4 ↓ --------------------------------------

print(f'\033[37m-------------------------- ↓ \033[34mtry/except - exemplo 4\033[37m ↓ --------------------------'
      f'\n\033[0m')

#  Forma 1
print(f'\033[37m--------------------------------- ↓ Forma 1\033[37m ↓ ----------------------------------'
      f'\n\033[0m')
try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')  # Geralmente guardado em Logs.

#  Forma 2
print(f'\n\033[37m--------------------------------- ↓ Forma 2\033[37m ↓ ----------------------------------'
      f'\n\033[0m')
try:
    len(5)
except TypeError as err:
    error_message = f'A aplicação gerou o seguinte erro: {err}'
    print(f'try: \nlen(5) \n\033[31mexcept TypeError as err: \033[0m \nprint("{error_message}")')
