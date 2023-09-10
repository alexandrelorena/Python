"""
tipo_booleano

True, False >> sempre a letra maiúscula
"""
ativo = True
print(ativo, '\n')

ativo = False
logado = False

print('está ativo? ', ativo, '\n')

"""
Operações básicas
"""
# Negação (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso.
Se for falso, o resultado será verdadeiro.
"""
print("------- NOT --------")
print(not ativo)

# Ou (or):Um ou outro deve ser vetdadeiro.
"""
É uma operação binária, ou seja, depende de dois valores. 

True or True -> True
True or False -> True
False or True -> True
False or False -> False

"""
print("------- OR --------")
print(True or True)
print(True or False)
print(False or True)
print(False or False, '\n')

print('está ativo ou logado?', (ativo or logado), '\n')

# E (and): ambos devem ser veerdadeiros.

"""
True and True -> True
True and False -> FFalse
False and True -> False
False and False -> False
"""
print("------- AND --------")
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print("---------------")

# Números

print('5 é menor que 6?', 5 < 6, '\n')
print('5 é maior ou igual a 6?', 5 >= 6, '\n')
print('5 é igual a 5?', 5 == 5, '\n')

num1 = 7
num2 = 8

print('num1 é igual num2?', num1 == num2, '\n')
print('num1 é menor que num 2 ou maior que 3?', num1 < num2 or num1 > 3, '\n')
print('num1 é menor que num 2 e maior que 3?', num2 > num1 > 3, '\n')  # num1 < num2 and num1 > 3

print('Tipo True é:', type(True))
print('Tipo False é:', type(False))

