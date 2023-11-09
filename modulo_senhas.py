#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
modulo_senhas
"""

from rich.console import Console
from passlib.hash import pbkdf2_sha256 as cryp

# -------------------------------------------- ↓ Bloco título ↓ --------------------------------------------
console = Console()

console.print()
texto = 'Trabalhando com senhas'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto

console.print(f'[on yellow][bold white][center]' + texto_centralizado)

# -------------------------------------------- ↑ Bloco título ↑ --------------------------------------------

texto = 'Métodos de Instância'
tamanho_desejado = 90  # Largura do bloco
texto_centralizado = texto.center(tamanho_desejado)  # Centralize o texto
console.print(f'[yellow]-' * 90)
console.print(f'[bold white][center]' + texto_centralizado)
console.print(f'[yellow]-' * 90)


class Usuario:

    def __init__(self, nomeuser, sobrenomeuser, emailuser, senhauser):
        self.__nomeuser = nomeuser
        self.__sobrenomeuser = sobrenomeuser
        self.__emailuser = emailuser
        self.__senhauser = cryp.hash(senhauser, rounds=2000000, salt_size=16)

    def nome_completo(self):
        return f'{self.__nomeuser} {self.__sobrenomeuser}'

    def checa_senha(self, senhauser):
        if cryp.verify(senhauser, self.__senhauser):
            return True
        return False


user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')

user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '654321')

print(user1.nome_completo())  # o 'self' é o user1

print(Usuario.nome_completo(user1))  # o passando a classe 'Usuario e a instância 'nome_completo'.

print(user2.nome_completo())  # o 'self' é o user2

nome = input('\n\nInforme o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

user = None

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere!!!')
    exit(1)

print('Usuário criado com sucesso"')

senha_acesso = input('Informe a senha para acesso: ')


if user.checa_senha(senha_acesso):
    print('Acesso permitido')

else:
    print('Acesso negado!!!')
