#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
modulo_pygments
"""
from pygments import highlight
from pygments.formatters.terminal import TerminalFormatter
from pygments.lexers.python import PythonLexer

code = """class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False
"""

colored_code = highlight(code, PythonLexer(), TerminalFormatter())

print(colored_code)
