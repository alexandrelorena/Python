"""
Definindo Funções

- Pequenas partes de código que realizam tarefas específicas.
- Pode ou não receber entradas de dados e retornar uma saída de dados.
- Muito úteis para executar procedimentos similares repetidas vezes.

"""
#  Exemploe de utilização de funções:

cores = ['verde', 'amarelo', 'azul', 'branco']

#  Utilizando a função integrada (Built-in)

print(cores)

curso = 'Programação em Python: Essencial'

print(curso)

cores.append('roxo')

print(cores)

# curso.append('Mais dados...')  # AttributeError

# print(curso)

cores.clear()
print(cores)

# print(help(print()))

#  DRY - Don1t repeat yourself - Não repita  seu código

print('\n----------------------Definindo Função------------------\n")
"""
def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

- parametros_de_entrada >> são pcinais
- bloco_da_funcao >> onde o processamento da funcao acontece. Tem ou não o retorno da função.
- utilizamos a palavra reservada "def".
"""


def diz_oi():
    print('oi!')


print('\n----------------------Utilizando a Função------------------\n")

diz_oi()  # Não esqueceer dos parênteses ao executar a função


def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')


# cantar_parabens()

# for n in range(5):  # executando a função em loop
#     cantar_parabens()

canta = cantar_parabens  # variável recebendo a função
canta()
