
"""
Módulo Collections - Counter (contador)

Collections >> High-performance Container Datetypes

counter -> recebe um iterável como parâmetro e cria um objeto do tipo Collections
Counter, que é parecido com um dicionário, contendo uma chave e o elemento da lista
passada como parâmetro e como valor a quantidade de ocorrências desses elementos.


"""
#  Realizando o import
from collections import Counter

#  Exemplo 1
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 43, 34]

#  Utilizanndo o counter
res = Counter(lista)

print(type(res))
#  <class 'collections.Counter'>
print(res)
# Counter({1: 5, 2: 5, 3: 5, 5: 4, 4: 3, 45: 2, 66: 1, 43: 1, 34: 1})

#  Exemplo 2

print(Counter('Geek University'))
#  Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

#  Exemplo 3
texto = """A Lei do Sorteio introduziu o serviço militar obrigatório para as Forças Armadas do Brasil, implantado de 
fato em 1916, substituindo o recrutamento forçado, o antigo “tributo de sangue”, e permitindo a constituição de uma 
reserva. O sorteio foi mecanismo de recrutamento de praças de 1916 a 1945, quando foi substituído pela convocação geral 
por classe, que é o modelo de serviço militar obrigatório existente no Brasil no século XXI."""

palavras = texto.split()
print(palavras)
#  ['A', 'Lei', 'do', 'Sorteio', 'introduziu', 'o', 'serviço', 'militar', 'obrigatório', 'para', 'as', 'Forças',
#  'Armadas', 'do', 'Brasil,', 'implantado', 'de', 'fato', 'em', '1916,', 'substituindo', 'o', 'recrutamento',
#  'forçado,', 'o', 'antigo', '“tributo', 'de', 'sangue”,', 'e', 'permitindo', 'a', 'constituição', 'de', 'uma',
#  'reserva.', 'O', 'sorteio', 'foi', 'mecanismo', 'de', 'recrutamento', 'de', 'praças', 'de', '1916', 'a', '1945,',
#  'quando', 'foi', 'substituído', 'pela', 'convocação', 'geral', 'por', 'classe,', 'que', 'é', 'o', 'modelo', 'de',
#  'serviço', 'militar', 'obrigatório', 'existente', 'no', 'Brasil', 'no', 'século', 'XXI.']

res = Counter(palavras)
print(res)
# Counter({'de': 7, 'o': 4, 'do': 2, 'serviço': 2, 'militar': 2, 'obrigatório': 2, 'recrutamento': 2, 'a': 2, 'foi': 2,
# 'no': 2, 'A': 1, 'Lei': 1, 'Sorteio': 1, 'introduziu': 1, 'para': 1, 'as': 1, 'Forças': 1, 'Armadas': 1, 'Brasil,': 1,
# 'implantado': 1, 'fato': 1, 'em': 1, '1916,': 1, 'substituindo': 1, 'forçado,': 1, 'antigo': 1, '“tributo': 1,
# 'sangue”,': 1, 'e': 1, 'permitindo': 1, 'constituição': 1, 'uma': 1, 'reserva.': 1, 'O': 1, 'sorteio': 1,
# 'mecanismo': 1, 'praças': 1, '1916': 1, '1945,': 1, 'quando': 1, 'substituído': 1, 'pela': 1, 'convocação': 1,
# 'geral': 1, 'por': 1, 'classe,': 1, 'que': 1, 'é': 1, 'modelo': 1, 'existente': 1, 'Brasil': 1, 'século': 1,
# 'XXI.': 1})

print(type(res))
# <class 'collections.Counter'>

# printando 5 palavras com mais ocorrências no texto
print(res.most_common(5))
# [('de', 7), ('o', 4), ('do', 2), ('serviço', 2), ('militar', 2)]

