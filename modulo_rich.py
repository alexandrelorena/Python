#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
modulo_rich
"""
from rich.console import Console
from rich.text import Text
from rich import print

# Crie uma instância da classe Console
console = Console()

# Crie um objeto Text para formatação de texto
texto_formatado = Text("Texto formatado com Rich")
texto_formatado.stylize("bold underline red on black")

# Use o método print para exibir o texto no console
print(texto_formatado)

# Você também pode imprimir texto simples com cores
# Texto colorido
print("[bold red]Texto em vermelho[/]")  # Encerra a formatação
print("[bold blue]Texto em azul[/]")  # Encerra a formatação
print("[bold green]Texto em verde[/]")  # Encerra a formatação

print("[bold yellow]Texto em amarelo[/]")


Text("[bold red]Texto em vermelho[/bold red]")
print("[bold blue]Texto em azul[/bold blue]")
print("[bold green]Texto em verde[/bold green]")

print("[on yellow]Teste[/] [bold red]de[/] [bold blue]cores[/]")

print(':warning: ola que legal')
