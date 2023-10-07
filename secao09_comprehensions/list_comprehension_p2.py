"""
list_comprehension - parte 2

- Podemos adicionar estruturas condicionais lógicas

# Síntaxe da List Comprehension

[ dado for dado in iterável ]

"""

print('\n------------- ↓ Exemplo 1 - pares e ímpares ↓ -------------\n')

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]

impares = [numero for numero in numeros if numero % 2 != 0]

print(f'Números pares: {pares}')

print(f'Números ímpares: {impares}')

print('\n------------- ↓ Exemplo 1 - refatorando ↓ -------------\n')

pares = [numero for numero in numeros if not numero % 2]  # Par >> FALSE (negação do módulo de 2)

impares = [numero for numero in numeros if numero % 2]  # Ímpar >> TRUE

print(f'Números pares: {pares}')

print(f'Números ímpares: {impares}')

print('\n------------- ↓ Exemplo 2 - dividindo impar e multiplicando par ↓ -------------\n')

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]

print(res)