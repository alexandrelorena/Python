"""
Funções com parâmetro padrão (Default parameters)

- passagem de parâmetro é opcional

"""
print('\n---------------- ↓ Ex de função com passagem de parâmetro opcional ↓ ----------------\n')

print('Geek University')

print()

print('\n---------------- Ex de função com passagem de parâmetro obrigatória ----------------\n')

print('\n---------------- ↓ Ex 1 - quadrado ↓ ----------------\n')


def quadrado(numero1):  # parãmetro obrigatório
    return numero1 ** 2


print(quadrado(3))
# print(quadrado()) - parãmetro obrigatório
# TypeError: quadrado() missing 1 required positional argument: 'numero'

print('\n---------------- ↓ Ex 2 - exponencial ↓ ----------------\n')

numero = 2  # Defina 'numero' fora da função


def exponencial(num=None, potencia=2):
    if num is None:
        num = numero  # Valor padrão se nenhum número for fornecido
    return num ** potencia


print(f' 2 elevado a 3 =  {exponencial(2, 3)}')

print(f' 3 elevado a 2 =  {exponencial(3, 2)}')


print('\n-------------------------------\n')
print(f'3 ao quadrado = {exponencial(3)}')  # por padrão eleve ao quadrado
print('\n-------------------------------\n')
print(f'3 elevado a 5 = {exponencial(3, 5)}')  # eleva a potência informada pelo usuário
print('\n-------------------------------\n')
print(f'numero {numero} ao quadrado = {exponencial()}')


print('\n---------------- ↓ parâmetros com valor default, SEMPRE ao final ↓ ----------------\n')


def teste(potencia, num=2):  # potencia é fornecida abaixo >> print(teste(6))
    return num ** potencia


print(teste(6))

print('\n-------------------------------\n')


def soma(num1, num2):
    return num1 + num2


print(soma(4, 3))  # argumentos obrigatórios

"""print(soma(4))  # TypeError

print(soma())  # TypeError"""

print('\n-------------------------------\n')

number1 = 5
number2 = 4


def soma(n1=None, n2=None):
    if n1 is None:
        n1 = number1
    if n2 is None:
        n2 = number2
    return n1 + n2


print(f'A soma de {number1} + {number2} = {soma(number1, number2)}')

print('\n-------------------------------\n')
print(soma(4))  # aqui o numero 1 é 4 e o numero 2 é o valor da variável number2
print('\n-------------------------------\n')
print(soma())  # aqui a soma é feita com os valores das variáveis number1 e number2

print('\n---------------- ↓  ↓ ----------------\n')


def mostra_informacao(nome='Geek', inst=False):
    if nome == 'Geek' and inst:
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Pensei que você fosse o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(inst=True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephany'))

print('\n---------------- ↓ Funções como parâmetro ↓ ----------------\n')


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))

print('\n---------------- ↓ Escopo - evitar problemas e confusões ↓ ----------------\n')

instrutor = 'Geek'  # Variável global


def diz_oi():
    inst = 'Python'  # variável local >> ela se sobrepõe a variável global
    return f'Oi {inst}'


print(diz_oi())

print('\n---------------- ↓  ↓ ----------------\n')


def diz_oi():
    prof = 'Geek'  # Variável local
    return f'Olá {prof}'


print(diz_oi())

# print(prof)  # NameError

print('\n---------------- ↓ ATENÇÃO com variáveis globais - tentar evitar ↓ ----------------\n')

total = 0

"""def incrementa():
    total = total + 1  # UnboundLocalError - variável local seno usada sem ter sido inicializada
    return total

print(incrementa())"""


def incrementa():
    global total  # Avisando que é pra usar variável global
    total = total + 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())


print('\n---------------- ↓ Funções declaradas dentro de função ↓ ----------------\n')


def fora():
    contador = 1

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())
