
"""
escopo_variaveis

Dois casos de escopo:

1 - Variáveis globais;
    - compreende todo o programa

2 - Variáveis locais;
    - está limitado ao bloco onde foi declarada.

"""
numero = 2  # ex de variável global
print(numero)
print(type(numero))

if numero > 10:
    novo = numero + 10  # ex de escopo local
    print(novo)

# print(novo)