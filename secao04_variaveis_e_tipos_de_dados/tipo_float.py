
"""
tipo_float

tipo real, decimal

- casas decimais:
o separador é o . (ponto)

valor = 1.44
print(valor)
1.44
------------------------
print(type(valor))
<class 'float'>
------------------------
valor1, valor2 = 1, 44
valor1
1
valor2
44
------------------------

"""
# Dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Conversão de float para inteiro
valor = 1.94

print(valor)
print(type(valor))

res = int(valor)  # Conversão

# Na conversão é ignorado o que está após o ponto
print(res)
print(type(res))

# Números complexos
variavel = 5j
print(variavel)
print("o tipo da variável", variavel, 'é: ',  type(variavel))

variavel = variavel **2
print(variavel)
