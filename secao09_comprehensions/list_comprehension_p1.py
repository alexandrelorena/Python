
"""
list_comprehension - parte 1

- Podemos gerar novas listas com dados processados a partir de outro iterável.

# Síntaxe da List Comprehension

[ dado for dado in iterável ]

"""

print('\n---------------- ↓ List Comprehension - multiplicação ↓ ----------------\n')

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

print('\n---------------- ↓ List Comprehension - divisão ↓ ----------------\n')

res = [numero / 2 for numero in numeros]

print(res)

print('\n---------------- ↓ List Comprehension - quadrado ↓ ----------------\n')


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]

print(res)

print('\n---------------- ↓ List Comprehension x Loop ↓ ----------------\n')

numeros = [1, 2, 3, 4, 5]  # bloco loop

numeros_dobrados = []  # bloco loop

"""for numero in numeros:  # bloco loop
    numero_dobrado = numero * 2  # bloco loop
    numeros_dobrados.append(numero_dobrado)  # bloco loop
"""
for numero in numeros:  # bloco loop
    numeros_dobrados.append(numero * 2)  # bloco loop

print(f'Utilizando LOOP:  {numeros_dobrados}\n')  # bloco loop

print('----------------------------------------\n')  # bloco loop

print(f'List Comprehension: {[numero * 2 for numero in numeros]}')

print('\n---------------- ↓ outros exemplos - 1 ↓ ----------------\n')

nome = 'Geek University'

print([letra.upper() for letra in nome])

print('\n------------ ↓ 2 - com função ↓ -----------\n')


def caixa_alta(nome2):
    nome2 = nome2.replace(nome2[0], nome2[0].upper())
    return nome2


amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([caixa_alta(amigo) for amigo in amigos])

print('\n------------- ↓ com capitalize() ↓ -------------\n')

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([amigo.capitalize() for amigo in amigos])

print('\n------------ ↓ 3 - tabuada do 3 ↓ -----------\n')

print([numero * 3 for numero in range(1, 11)])

print('\n------------ ↓ 4 - booleanos ↓ -----------\n')

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

print('\n------------ ↓ 5 - transformando em string ↓ -----------\n')

print([str(numero) for numero in [1, 2, 3, 4, 5]])
