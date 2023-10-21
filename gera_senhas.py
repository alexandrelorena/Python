"""
gera_senhas
"""
import random
import string

print(f'\n\033[32m----------------------------- ↓ \033[36mGerador de senhas\033[32m ↓ -----------------------------'
      f'\n\033[35m')


def generate_password(length=8):
    # Caracteres possíveis para cada categoria
    letters_upper = string.ascii_uppercase
    letters_lower = string.ascii_lowercase
    digits = string.digits
    special_chars = '!@#$%^&*'

    # Certifique-se de que o comprimento mínimo seja 8
    if length < 8:
        length = 8

    # Crie uma lista de caracteres
    all_chars = (list(letters_upper) +
                 list(letters_lower) +
                 list(digits) +
                 list(special_chars))

    # Garanta que pelo menos um de cada categoria esteja presente
    password = [random.choice(letters_upper),
                random.choice(letters_lower),
                random.choice(digits),
                random.choice(special_chars)]

    # Preencha o restante da senha com caracteres aleatórios
    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    # Embaralhe a senha para torná-la mais aleatória
    random.shuffle(password)

    # Converta a lista em uma string
    password = ''.join(password)

    return password


# Exemplo de uso para gerar uma senha de 12 caracteres
password = generate_password(13)
print(password)
