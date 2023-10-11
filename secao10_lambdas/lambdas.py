"""
Utilizando Lambdas

Funções sem nome, ou seja, funções anônimas.

# Função em Python:

def soma(a, b):
    return a + b


"""

print('\n------------- ↓ Ex de Função em Python ↓ -------------\n')


def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))

print('\n------------- ↓ Expressão Lambda ↓ -------------\n')

lambda x: 3 * x + 1

calc = lambda x: 3 * x + 1

print(calc(5))
print(calc(8))

print('\n------------- ↓ Expressão Lambda com múltiplas entradas ↓ -------------\n')

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
# strip() remove espaços no início e no fim da variável
# title() transforma a inicial em maiúscula

print(nome_completo(' angelina', 'JOLIE'))
print(nome_completo('  FELICITY       ', ' jones '))

print('\n------------- ↓ Expressões Lambda ↓ -------------\n')

amar = lambda: 'Como não amar Python?'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x1, ....,  xn: <expressão>

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

print('\n------------- ↓ Expressões Lambda - autores por ordem de sobrenome↓ -------------\n')

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinley', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

# print(f'{autores}\n')


autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

print('\n------------- ↓ Expressões Lambda - Função quadrática ↓ -------------\n')

# f(x) = a * x ** 2 + b * x + c


def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))


print(geradora_funcao_quadratica(3, 0, 1)(2))