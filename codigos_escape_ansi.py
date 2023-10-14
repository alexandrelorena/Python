
"""
codigos_escape_ansi
"""
print('\n')
print(f"\033[30m Cor: branco\033[0m" "\033[37m | cinza \033[0m" "\033[90m | cinza-escuro \033[0m" "\033[97m | preto \n\033[0m")

print(f"\033[31m Cor: vermelho\033[0m" "\033[91m | vermelho-claro \n\033[0m")

print(f"\033[92m Cor: verde\033[0m" "\033[32m | verde\033[0m" "\033[36m | verde-claro \n\033[0m")

print(f"\033[34m Cor: azul\033[0m" "\033[96m | azul-claro\033[0m" "\033[94m | azul \n\033[0m")

print(f"\033[33m Cor: amarelo\033[0m" "\033[93m | amarelo \n\033[0m")

print(f"\033[35m Cor: roxo \n\033[0m")

print(f"\033[95m Cor: rosa \n\033[0m")

print(f"\033[40;97m fundo: branco | texto: preto\n\033[0m")

print(f"\033[47;97m fundo: cinza | texto: preto\n\033[0m")

print(f"\033[100;97m fundo: cinza-escuro | texto: preto\n\033[0m")

print(f"\033[107;30m fundo: preto | texto: branco\n\033[0m")

print(f"\033[41;97m fundo: vermelho | texto: preto\n\033[0m")

print(f"\033[101;97m fundo: vermelho-claro | texto: preto\n\033[0m")

print(f"\033[42;97m fundo: verde-abacate 1 | texto: preto\n\033[0m")

print(f"\033[102;97m fundo: verde-abacate 2 | texto: preto\n\033[0m")

print(f"\033[43;97m fundo: amarelo | texto: preto\n\033[0m")

print(f"\033[103;97m fundo: amarelo-claro | texto: preto\n\033[0m")

print(f"\033[44;97m fundo: azul | texto: preto \n\033[0m")

print(f"\033[104;97m fundo: azul-claro | texto: preto \n\033[0m")

print(f"\033[45;97m fundo: rosa | texto: preto\n\033[0m")

print(f"\033[105;97m fundo: rosa | texto: preto\n\033[0m")

print(f"\033[46;97m fundo: verde-água 1 | texto: preto\n\033[0m")

print(f"\033[106;97m fundo: verde-água 2 | texto: preto\n\033[0m")

print('\033[30;3mEste texto está em itálico.\033[0m\n')

print('\033[30;4mEste texto está sublinhado.\033[0m')

""" 
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
