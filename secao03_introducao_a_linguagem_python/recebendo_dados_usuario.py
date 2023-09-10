"""
Recebendo dados do usuário
input() -> Todo dado recebido via input é do tipo string

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:

'angelina'
"angelila"
'''angelina'''
"""
# """angelina"""


# Entrada de dados
"""print("Qual seu nome? ")
nome = input()"""

# Entrada de dados simplificada
nome = input('Qual seu nome? ')


# Exemplo de print antigo - 2.x
# print('Seja bem-vindo(a) %s' % nome)
# ------------------------------------
# Exemplo de print moderno - 3.x
# print('Seja bem-vindo(a) {0}'.format(nome))
# ------------------------------------
# Exemplo de forma atual - 3.7
print(f'Seja bem-vindo(a) {nome.title()}')


"""print("Qual sua idade? ")
idade = input()"""

# Entrada de dados simplificada
idade = int(input('Qual sua idade? '))  # Cast ( alterando de string para inteiro

# Processamento

# saída de dados
# Exemplo de print antigo - 2.x'
# print('%s tem %s anos' % (nome, idade))
# ------------------------------------
# Exemplo de print moderno - 3.x
# print('{0} tem {1} anos'.format(nome, idade))
# ------------------------------------
# Exemplo de forma atual - 3.7
print(f'{nome.title()} tem {idade} anos')

""" 
int(idade) => cast

Cast é a conversão de um tipo de dado para outro.

"""
print("------------------------------------------")
print(f'{nome.title()} tem {idade} anos e nasceu em {2023 - idade}')  # int(idade) => cast
print("------------------------------------------")
