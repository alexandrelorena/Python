"""
tipo_string

'uma string', '234', 'a', 'True', '42.4'

"uma string", "234", "a", "True", "42.4"

'''uma string''', '''234''', .....
"""
# """uma string""", """234"""

nome = 'Geek'
print(nome)
print(type(nome))

print('\n----------------\n')

nome = "Gina's Bar"
print(type(nome))
print(nome)

print('\n----------------\n')

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

print('\n----------------\n')

nome = """ Angelina 
Jolie"""
print(nome)
print(type(nome))

print('\n----------------\n')

nome = 'Angelina " Jolie'
print(nome)
print(type(nome))

print('\n----------------\n')

nome = 'Angelina Jolie'  # upper case
print(nome.upper())
print(type(nome))

print('\n----------------\n')

nome = 'Angelina Jolie'  # lower case
print(nome.lower())
print(type(nome))

print('\n----------------\n')

nome = 'angelina jolie'  # title case
print(nome.title())
print(type(nome))

print('\n----------------\n')

nome = 'angelina jolie'  # split / lista
print(nome.split())
print(type(nome))

#  Listas
#  [ 0,   1,   2,   3 ]
#  ['G', 'e', 'e', 'k']
print('\n----------------\n')

nome = 'Geek University'
print(nome[0:4])  # Slice de String
print(nome[5:15])  # Slice de String
print(type(nome))
print('\n----------------\n')
print(nome.split())
print('\n----------------\n')
print(nome.split()[1])

print(nome[::-1])  # Inversão da string / primeiro ao ultimo elemento invertido.

print(nome.replace('e', '1'))
