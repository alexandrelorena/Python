
"""
loop_while

Forma geral

while expressao_booleana:
    //execução do loop

O bloco do while será repetid enquanto a expressão booleana(verdadeiro ou falso) for verdadeira.


"""

numero = 1
resposta = ''

# Ex 1
print('\033[97;40mExemplo 1: while numero < 10, print(numero), numero = numero + 1:\033[0m')
while numero < 10:
    print(numero)
    numero = numero + 1
print('------------------------------------')

# Ex 2
print('\033[97;40mExemplo 2: while numero < 10, print(numero), numero = numero + 1:\033[0m')
while resposta != 'sim':
    resposta = input('Já acabou Jéssica? ')

print('------------------------------------')
