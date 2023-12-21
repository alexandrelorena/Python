import tkinter as tk
from tkinter import filedialog
import os

class ProgramWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Programa Python")
        self.master.geometry("500x500")
        self.create_widgets()

    def create_widgets(self):
        self.text = tk.Text(self.master, wrap="word")
        self.text.pack(fill="both", expand=True)

        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Arquivo", menu=self.file_menu)
        self.file_menu.add_command(label="Abrir banco.py", command=self.open_banco_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Sair", command=self.master.quit)

    def open_banco_file(self):
        # Caminho do arquivo 'banco.py'
        banco_path = r"C:\Users\DXC\Documents\Alexandre\pythonProject\projetos\banco\banco.py"

        try:
            with open(banco_path, "r") as f:
                self.text.delete("1.0", "end")
                self.text.insert("1.0", f.read())
        except FileNotFoundError:
            print("Arquivo 'banco.py' não encontrado.")
        except Exception as e:
            print(f"Erro ao abrir 'banco.py': {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProgramWindow(root)
    root.mainloop()
