
"""
estruturas_logicas_and_or_not_is

Operadores unários:
    - not, is

Operadores binários:
    - and, or

"""
ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo usuário!')
else:
    print('Você precis ativar sua conta. Por favor, cheque seu e-mail')


print('--------------------------')


if ativo or logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')


print('--------------------------')


if not ativo:
    print('Você precis ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário!')


print('--------------------------')


if ativo:
    print('Bem-vindo usuário!')
else:
    print('Você precis ativar sua conta. Por favor, cheque seu e-mail')


print('--------------------------')

print(ativo is False)

print('--------------------------')
