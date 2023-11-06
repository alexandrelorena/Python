from rainbowstream import highlight

# Código que você deseja realçar
code = """class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False
"""

# Realce o código
highlighted_code = highlight(code, language='python')

# Imprima o código realçado
print(highlighted_code)
