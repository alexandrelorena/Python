#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
modulo_pygments
"""
from pygments import highlight
from pygments.formatters.terminal import TerminalFormatter
from pygments.lexers.python import PythonLexer
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from rich.console import Console
from rich.syntax import Syntax
from rich.theme import Theme

# Defina o tema do terminal
custom_theme = Theme({
    "code.comment": "bold cyan",
    "code.keyword": "bold blue",
    "code.literal": "bold yellow",
    "code.identifier": "bold green",
    "code.string": "bold green",
})


def print_colored_code(code, language="python"):
    # Use o Pygments para realçar a sintaxe do código
    lexer = get_lexer_by_name(language, stripall=True)
    colored_code = highlight(code, lexer, TerminalFormatter())

    # Use o Rich para imprimir o código com formatação adicional
    syntax = Syntax(colored_code, language)

    console = Console(theme=custom_theme)
    console.print(syntax)


if __name__ == "__main__":
    code_to_print = """class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self ligada = False
    """
    print_colored_code(code_to_print, "python")