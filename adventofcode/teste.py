import re
from input_data import input_data

# Lista de linhas de entrada
linhas = input_data.split('\n')

# Inicializa a soma total
soma_total = 0

# Processa cada linha
for linha in linhas:
    # Encontra todos os números na linha usando expressões regulares
    numeros = re.findall(r'\d+', linha)

    # Se existem números na linha
    if numeros:
        # Soma o primeiro e o último número
        soma_total += float(numeros[0]) + float(numeros[-1])

print(soma_total)
