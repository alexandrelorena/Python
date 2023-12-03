#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Introdução ao módulo Unittest => Testes unitários
— Forma de se testar unidades individuais de código-fonte.
— Unidades individuais podem ser: funções, métodos, classes, módulos, etc.

Teste unitário não é exclusivo do Python

— Para criar os testes, criamos classes que herdam de unittest.
— Para criarPara rodar os testes, utilizamos unittest.main()
— TestCase => Casos de teste para sua unidade

# Conhecendo as Assertions

| Método                    | Assert                |
|---------------------------|-----------------------|
| assertEqual(a, b)         | a == b                |
| assertNotEqual(a, b)      | a != b                |
| assertTrue(x)             | x is True             |
| assertFalse(x)            | x is False            |
| assertIs(a, b)            | a is b                |
| assertIsNot(a, b)         | a is not b            |
| assertIsNone(x)           | x is None             |
| assertIsNotNone(x)        | x is not None         |
| assertIn(a, b)            | a in b                |
| assertNotIn(a, b)         | a not in b            |
| assertIsInstance(a, b)    | isinstance(a, b)      |
| assertNotIsInstance(a, b) | not isinstance(a, b)  |
| assertGreater(a, b)       | a > b                 |
| assertLess(a, b)          | a < b                 |
| assertGreaterEqual(a, b)  | a >= b                |
| assertLessEqual(a, b)     | a <= b                |

"""
from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Introdução ao módulo Unittest'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ Utilizando a abordagem TDD ↓
# --------------------------------------------------------------------------------------------------------------------



console.print("[yellow]#---------------------------------------------------------------------\n")
