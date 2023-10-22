"""
Funções com retorno

- Pequenas partes de código que realizam tarefas específicas.
- Pode ou não receber entradas de dados e retornar uma saída de dados.
- Muito úteis para executar procedimentos similares repetidas vezes.

"""

numeros = [1, 2, 3]

# numeros.pop()  # remove o último elemento da lista

print(numeros)
print(type(numeros))

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

"""ret_pr = print(numeros)   # não retorna nenhum valor >> none

print(f'Retorno de print: {ret_pr}')"""

#  Exemplo de função
print("\n---------- Sem retorno-----------\n")


def quadrado_de_7():
    print(7 * 7)


"""ret = quadrado_de_7()  # não retorna nenhum valor >> none


print(f'Retorno: {ret}')"""


print("\n---------- Retornando valor-----------\n")


def sete_ao_quadrado():
    return 7 * 7

# variável recebendo retorno da função

# Forma 1


ret = sete_ao_quadrado()


print(f'Retorno: {ret}')

# Forma 2
print(f'Retorno: {sete_ao_quadrado() + 1}')  # fazendo operação matemática

print("\n---------- Refatorando a primeira função-----------\n")


def diz_oi():
    return 'Oi '


alguem = 'Pedro'

print(diz_oi() + alguem)

#  Exemplo 1


def diz_oi():
    print('Estou sendo executado ante do return')
    return 'Oi '  # a função pára aqui. O return finaliza a função.
    # print('Estou sendo executado após o return')


print(diz_oi())

#  Exemplo 2 - em uma função, podemos ter mais de 1 return


def nova_funcao():
    variavel = None
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())


#  Exemplo 3 - em uma função, podemos retornar qualquer tipo de dado e múltiplos valores.


def outra_funcao():
    return 2, 3, 4, 5  # recebendo 4 valores


num1, num2, num3, num4 = outra_funcao()  # colocando os valores nas variáveis

print(num1, num2, num3, num4)  # printando as variáveis - desempacotamento de tupla

print(outra_funcao())  # imprime no formato de tupla

print(type(outra_funcao()))
# <class 'tuple'>

print("\n---------- Função para jogar a moeda-----------\n")


from random import random


def joga_moeda():  # gera um número pseudo randômico entre 0 e 1
    valor = random()
    print(valor)
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())

print("\n---------- refatorando a Função joga_moeda-----------\n")


def joga_moeda():  # gera um número pseudo randômico entre 0 e 1

    if random() > 0.5:
        print(random())
        return 'Cara'
    return 'Coroa'


print(joga_moeda())


print("\n---------- codificação desnecessária-----------\n")


def eh_impar():
    numero = 6
    if numero % 2 != 0:
        return True
    # else:  esse 'else' é desnecessário nesse contexto
    return False


print(eh_impar())
