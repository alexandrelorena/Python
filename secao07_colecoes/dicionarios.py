
"""
dicionarios (ou mapas, em algumas linguagens de programação.

- coleções do tipo chave/valor
- são representados por chaves {}
- chave e valor separados por :  'chave:valor',
- qualquer tipo de dados
"""
print("-----------------------Criação de dicionários---------------------------")
# Forma 1 (mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguay'}
print(paises)
print(type(paises))

# Forma 2 (menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')
print(paises)
print(type(paises))

print("-----------------------Acessando elementos---------------------------")
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguay'}

# Forma 1 - via chave

print(paises['br'])
print(paises['py'])
# Forma 2 - via get (recomendado)

print(paises.get('br'))
print(paises.get('ru'))

pais = paises.get('ru', 'Não encontrado')

# if pais:
print(f'Encontrei o país {pais}')
# else:
#     print(f'Nã encontrei o país {pais}')

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

print("-----------------------Dicionário com tupla---------------------------")

localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 122.4194): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))

print("-----------------------Adicionar elementos em um dicionário---------------------------")

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 - Mais comum

receita['abr'] = 350

print(receita)

# Forma 2

novo_dado = {'mai': 500}

receita.update(novo_dado)  # receita.update({'mai': 200})

print(receita)

print("-----------------------Atualizando dados em um dicionário---------------------------")

# Forma 1

receita['mai'] = 550

print(receita)

# Forma 2

receita.update({'mai': 600})

print(receita)

print("-----------------------Remover dados em um dicionário---------------------------")

receita = {'jan': 100, 'fev': 120, 'mar': 300}

# Forma 1 - Mais comum
print(receita)

ret = receita.pop('mar')  # necessário informar SEMPRE a chave e KeyError é retornado caso não encontre o elemento.

print(ret) # retorna o valor que o elemento removido tinha

print(receita)

# Forma 2

del receita['fev']  # caso a chave não exista, será gerado KeyError
# Neste caso, o valor removido não é retornado

print(receita)

print("-----------------------Métodos de dicionário---------------------------")

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

#  limpar dicionário (zerar dados)

d.clear()

print(d)

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

print("-----------------------copiando um dicionário para outro - Forma 1 - Deep Copy---------------------------")

novo = d.copy()

print(novo)

novo['d'] = 4

print(d)
print(novo)

print("-----------------------copiando um dicionário para outro - Forma 2 - Shallow Coppy---------------------------")
# ambos são alterados no Shallow Copy
novo = d
print(novo)

novo['d'] = 4

print(d)
print(novo)

print("-----------------------Forma não usual de criação de dicionário---------------------------")

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parâmetros: um iterável e um valor
# Ir gerar uma chave pra cada valor iterável, e atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)
print(type(veja))

veja = {}.fromkeys(range(1, 11), 'novo')

print(veja)
print(type(veja))

print('--------------- Soma, valor máximo, valor mínimo, tamanho ---------------- ')

mat = {1, 2, 3, 4, 5, 6}

print(sum(mat))
print(max(mat))
print(min(mat))
print(len(mat))

