"""
Reduce

- A partir do Python3+ a função reduce() não é mais uma função integrada (built-in).
- Deve ser importada a partir do módulo 'functools'

reduce(funcao, dados) >> recebe o método com 2 valores

ex:

dados = [a1, a2, a3, ..., an]

def funcao(x, y):
    return x * y

passo 1: res1 = f(a1, a2) >> aolica a função nos dois primeiros elementos da coleção e guarda o resultado.
passo 2: res2 = f(res1, a3) >> aplica a função passando o resultdo do passo 2 + o terceiro elemento e gaurda o resultado

e assim por diante....

passo 3 : res3 f(res2, a4)
.
.
.
passo n: resn = f(resn, an)

Ou seja, é aplicada a função em cada passo, passando como primeiro argumento o resultado da aplicação anterior.
Até o reduce() retornar o resultado final.

"""
from functools import reduce
print('\n------------- ↓ Reduce ↓ -------------\n')

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(type(res))
print(res)

print('\n------------- ↓ Reduce usando loop normal ↓ -------------\n')

res = 1
for n in dados:
    res = res * n

print(res)

print('\n--------------------------\n')
