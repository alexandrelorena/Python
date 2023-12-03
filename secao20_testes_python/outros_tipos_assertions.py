#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Outros tipos de Assertions

assertNotEqual(a, b)

assertTrue(x)

assertFalse(x)
"""
from rich.console import Console

# ------------------------------------------------- ↓ Bloco título ↓ -------------------------------------------------

console = Console()

console.print()
texto = 'Outros tipos de Assertions'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on magenta][bold white][center]' + texto_centralizado)

# ------------------------------------------------- ↑ Bloco título ↑ -------------------------------------------------
# ↓ outros_tipos_assertions ↓
# --------------------------------------------------------------------------------------------------------------------

texto = '↓ Testes unitários - Utilizando a abordagem TDD ↓'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 70)
console.print(f'[bold yellow][center]' + texto_centralizado)
console.print(f'[yellow]-' * 70)


console.print("""
[white]— Forma de se testar unidades individuais de código-fonte.
— Unidades individuais podem ser: funções, métodos, classes, módulos, etc.

Teste unitário não é exclusivo do Python

— Para criar os testes, criamos classes que herdam de unittest.
— Para criarPara rodar os testes, utilizamos unittest.main()
— TestCase => Casos de teste para sua unidade
""")

texto = '↓ Conhecendo as Assertions ↓'
tamanho_desejado = 70  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 70)
console.print(f'[bold yellow][center]' + texto_centralizado)
console.print(f'[yellow]-' * 70)

console.print("""[cyan]
╔═══════════════════════════╦═══════════════════════════╗
║          Método           ║          Assert           ║
║═══════════════════════════╬═══════════════════════════║
║ assertEqual(a, b)         ║ a == b                    ║
║ assertNotEqual(a, b)      ║ a != b                    ║
║ assertTrue(x)             ║ x is True                 ║
║ assertFalse(x)            ║ x is False                ║
║ assertIs(a, b)            ║ a is b                    ║
║ assertIsNot(a, b)         ║ a is not b                ║
║ assertIsNone(x)           ║ x is None                 ║
║ assertIsNotNone(x)        ║ x is not None             ║
║ assertIn(a, b)            ║ a in b                    ║
║ assertNotIn(a, b)         ║ a not in b                ║
║ assertIsInstance(a, b)    ║ a is instance b           ║
║ assertNotIsInstance(a, b) ║ a not is instance b       ║
║ assertGreater(a, b)       ║ a > b                     ║
║ assertLess(a, b)          ║ a < b                     ║
║ assertGreaterEqual(a, b)  ║ a >= b                    ║
║ assertLessEqual(a, b)     ║ a <= b                    ║
╚═══════════════════════════╩═══════════════════════════╝
""")

console.print("[yellow]#---------------------------------------------------------------------")
console.print("""
[white]Por convenção, todos os testes em um test case, devem ter seu nome iniciado com teste_

Para executar os testes com unittest

    [blue]— python nome_do_modulo.py[/blue]

Para executar os testes com unittest no modo verbose

    [blue]— python nome_do_modulo.py -v[/blue]

Docstrings nos testes

    [blue]— Recomendado acrescentar Docstrings nos testes[/blue]    
""")

console.print("[yellow]#---------------------------------------------------------------------\n")
