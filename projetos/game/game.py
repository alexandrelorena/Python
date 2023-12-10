#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
game

"""
from rich.console import Console
from models.calcular import Calcular


# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------
#
console = Console()
#
# console.print()
# texto = 'game'
# tamanho_desejado = 70  # Largura do bloco
# texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
#
# console.print(f'[on magenta][bold white][center]' + texto_centralizado)
#
# console.print("[yellow]----------------------------------------------------------------------\n")

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ game ↓
# --------------------------------------------------------------------------------------------------------------------
def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    try:
        dificuldade_input: str = console.input(f'[white]Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: ')
        dificuldade: int = int(dificuldade_input)

        if dificuldade < 1 or dificuldade > 4:
            print('Nível inválido. Tente novamente.')
            return jogar(pontos)

        calc = Calcular(dificuldade)

        print('\nInforme o resultado para a seguinte operação: \n')
        calc.mostrar_operacao()

        resultado_input: str = input()
        resultado: int = int(resultado_input)

        if calc.checar_resultado(resultado):
            pontos += 1
            print()
            console.print(f'[green]Agora você tem {pontos} ponto(s).')
        else:
            print()
            console.print(f'[red]O resultado correto seria: {calc.resultado}')

    except ValueError:
        console.print("[bold red]Valor incorreto. Certifique-se de fornecer um número válido.")
        return jogar(pontos)

    except Exception as e:
        console.print(f"[bold red]Ocorreu um erro inesperado: {str(e)}")
        return jogar(pontos)

    while True:
        try:
            print()
            continuar: int = int(console.input('[magenta]Deseja continuar no jogo? [1 - sim, 0 - não] '))

            if continuar not in (0, 1):
                raise ValueError
            if continuar:
                print()
                jogar(pontos)
            else:
                print()
                console.print(f'Você finalizou com {pontos} ponto(s).')
                print()
                console.print('[blue]Até a próxima!')
            break
        except ValueError:
            console.print("[bold red]Valor incorreto!")
        except Exception as e:
            console.print(f"[bold red]Ocorreu um erro inesperado: {str(e)}")

if __name__ == '__main__':
    main()

