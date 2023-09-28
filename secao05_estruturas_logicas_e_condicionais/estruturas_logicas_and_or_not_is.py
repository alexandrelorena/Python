
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


print('\n--------------------------\n')


if ativo or logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')


print('\n--------------------------\n')


if not ativo:
    print('Você precis ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário!')


print('\n--------------------------\n')


if ativo:
    print('Bem-vindo usuário!')
else:
    print('Você precis ativar sua conta. Por favor, cheque seu e-mail')


print('\n--------------------------\n')

print(ativo is False)

print('\n--------------------------\n')
