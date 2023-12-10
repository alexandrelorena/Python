#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
calcular

"""
from rich.console import Console
from random import randint


# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()
#
# console.print()
# texto = 'calcular'
# tamanho_desejado = 70  # Largura do bloco
# texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
#
# console.print(f'[on magenta][bold white][center]' + texto_centralizado)
#
# console.print("[yellow]----------------------------------------------------------------------\n")

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ calcular ↓
# --------------------------------------------------------------------------------------------------------------------

class Calcular:

    def __init__(self: object, dificuldade: int, /) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 4)  # 1 = soma, 2 = subtração, 3 = multiplicação, 4 = divisão
        self.__resultado: int = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    def __str__(self: object) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'soma'
        elif self.operacao == 2:
            op = 'subtração'
        elif self.operacao == 3:
            op = 'multiplicação'
        elif self.operacao == 4:
            op = 'divisão'
        else:
            op = 'operação desconhecida'
        return f'Valor 1: {self.valor1} \nValor 2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperação: {op}'

    @property
    def _gerar_valor(self: object) -> int:
        if self.dificuldade == 1:
            return randint(0, 10)
        elif self.dificuldade == 2:
            return randint(0, 100)
        elif self.dificuldade == 3:
            return randint(0, 1000)
        elif self.dificuldade == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)

    @property
    def _gerar_resultado(self: object) -> int:
        if self.operacao == 1:  # soma
            return self.valor1 + self.valor2
        elif self.operacao == 2:  # subtracao
            return self.valor1 - self.valor2
        elif self.operacao == 3:  # multiplicação
            return self.valor1 * self.valor2
        else: # self.operacao == 4:  # divisão
            return self.valor1 / self.valor2
        # else:
        #     return 0
    @property
    def _op_simbolo(self: object) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        elif self.operacao == 3:
            return '*'
        else:
            return '/'


    def checar_resultado(self: object, resposta: int) -> bool:
        certo: bool = False

        if self.resultado == resposta:
            console.print('\n[green]Resposta correta!')
            certo = True
        else:
            console.print('\n[red]Resposta errada!')
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return certo

    def mostrar_operacao(self: object) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')

# console.print("[yellow]----------------------------------------------------------------------\n")
