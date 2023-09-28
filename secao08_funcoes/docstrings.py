
"""
Documentando funções com Docstrings

- Para ter acesso a documentação de uma função: __doc__;
- função help();

----------------------------------------------------------
from docstrings import diz_oi
diz_oi()
'Oi!'
help(diz_oi)
Help on function diz_oi in module docstrings:

diz_oi()
    Uma funþÒo simples que retorna a string 'OI'


print(diz_oi.__doc__)
Uma função simples que retorna a string 'OI'
-----------------------------------------------------------

"""


def diz_oi():
    """Uma função simples que retorna a string 'OI'"""
    return 'Oi!'


def exponencial(numero, potencia=2):
    """
    Função que retorna o quadrado de um número ou o número a potência informada.
    :param numero: número que desejamos gerar o exponencial.
    :param potencia: Potência que queremosgerar o exponencial. Por padrão é 2.
    :return: Returna o exponencial de 'numero' por potência.
    """
    return numero ** potencia


