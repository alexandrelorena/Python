"""
Filter

- recebe 2 parâmetros: 1 função e 1 iterável.

"""
import statistics  # Biblioteca para trabalhar com dados estatísticos

print('\n------------- ↓ Filter ↓ -------------\n')

valores = 1, 2, 3, 4, 5, 6

media = (sum(valores) / len(valores))

print(media)

print('\n--------------------------\n')

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()

media = statistics.mean(dados)

print(f'media: {media}')

print('\n--------------------------\n')

#                    função      iterável
res = filter(lambda x: x > media, dados)

print(list(res))

print('\n--------------------------\n')

res = filter(lambda x: x < media, dados)
print(type(res))
print(list(res))

print(f'Novamente: {list(res)}')
# Assim como no Map, após usado a primeira vez, o valor sai da memória e a lista fica vazia

print('\n------------ ↓ ex com Map ↓ -----------\n')

res = map(lambda x: x > media, dados)
print(type(res))
print(list(res))

print('\n------------ ↓ ex de Filter com dados faltantes ↓ -----------\n')

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colômbia', '', 'Equador', '', '', 'Venezuela']
print(paises)

print('\n------------ ↓ dados filtrados método 1 "None" ↓ -----------\n')

res = filter(None, paises)

print(list(res))

print('\n------------ ↓ dados filtrados método 2 "Lambda" ↓ -----------\n')

res = filter(lambda pais: len(pais) > 0, paises)

print(list(res))

print('\n------------ ↓ dados filtrados método 3 "For" ↓ -----------\n')

res = filter(lambda pais: pais != '', paises)

print(list(res))

print('\n------------ ↓ Diferenças entre map() e filter() ↓ -----------\n')

#  map() >> Recebe 2 parâmetros (função e iterável) e retorna um objeto mapeando a função para cada elemento iterável.
#  map() mostra valores booleanos
#  filter() >> Recebe 2 parâmetros (função e iterável) e retorna um objeto filtrando apenas os elementos
#  filter() mostra true ou false

print('\n------------ ↓ exemploes complexos ↓ -----------\n')

usuarios = [  # cada elemento nessa lista é um dicionário
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo gatos"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gost de cachorros", "Eu vou sair hoje"]},
    {"username": "gal", "tweets": []}
]
print(type(usuarios))
print(usuarios)

print('\n-------- ↓ filtrando usuários inativos - forma 1 ↓ -------\n')

inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

print(inativos)

print('\n-------- ↓ filtrando usuários inativos - forma 2 ↓ -------\n')

inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)

print('\n-------- ↓ Combinando filter() e map() ↓ -------\n')

nomes = ['Vanessa', 'Ana', 'Maria']
#  criar uma lista contendo 'Sua instrutora é' + nome, com nome tendo menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é: {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)

