
"""
codigos_escape_ansi
"""
"""Cores de Texto (Texto/Frente):

\033[30m: Branco
\033[31m: Vermelho
\033[32m: Verde
\033[33m: Amarelo
\033[34m: Azul
\033[35m: Magenta (Roxo)
\033[36m: Ciano (Azul Claro)
\033[37m: Cinza

Cores de Texto mais Claras (Texto/Frente):

\033[90m: Cinza Escuro
\033[91m: Vermelho Claro
\033[92m: Verde Claro
\033[93m: Amarelo Claro
\033[94m: Azul Claro
\033[95m: Magenta Claro (Roxo Claro)
\033[96m: Ciano Claro (Azul Claro)
\033[97m: Preto

Cores de Fundo:

\033[40m: Branco
\033[41m: Vermelho
\033[42m: Verde
\033[43m: Amarelo
\033[44m: Azul
\033[45m: Magenta (Roxo)
\033[46m: Ciano (Azul Claro)
\033[47m: Preto

Cores de Fundo mais Claras:

\033[100m: Cinza Escuro
\033[101m: Vermelho Claro
\033[102m: Verde Claro
\033[103m: Amarelo Claro
\033[104m: Azul Claro
\033[105m: Magenta Claro (Roxo Claro)
\033[106m: Ciano Claro (Azul Claro)
\033[107m: Preto

Estilos de Texto:

\033[0m: Reset (remove todos os estilos).
\033[1m: Negrito.
\033[2m: Faint (texto mais claro). não funciona no pycharm
\033[3m: Itálico (nem sempre suportado).
\033[4m: Sublinhado.
\033[5m: Pisca-pisca (texto em movimento).  não funciona no pycharm
\033[7m: Inverte as cores do texto e do fundo.
\033[8m: Esconde o texto (nem sempre suportado).

Limpar a Tela:

\033[2J: Limpa a tela.
Posicionar o Cursor:

\033[<linha>;<coluna>H: Move o cursor para a posição especificada.

Ocultar/Exibir o Cursor:

\033[?25l: Oculta o cursor.
\033[?25h: Exibe o cursor."""

print('###################################################')

print('\033[97;43mEste texto está na cor preta com o fundo amarelo\033[0m')

print('###################################################')

print('\033[31;107mEste texto está na cor vermelha com o fundo preto\033[0m')

print('###################################################')

print('\033[30;41mEste texto está na cor branca com o fundo vermelho\033[0m')

print('###################################################')

print('\033[30;3mEste texto está em itálico.\033[0m')

print('###################################################')

print('\033[30;4mEste texto está sublinhado.\033[0m')
