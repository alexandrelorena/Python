#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
banco

"""

from typing import List
from time import sleep
from projetos.banco.models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []

# console = Console()
def main() -> None:
    menu()

def menu() -> None:
    print('\033[36m╔═══════════════════════════════╗')
    print('╠═════════════ ATM ═════════════╣')
    print('╠══════════ Geek Bank ══════════╣')
    print('╠═══════════════════════════════╣')
    print('║  Selecione uma opção no menu  ║')
    print('╠═══════════════════════════════╣')
    print('║    1 - Criar conta            ║')
    print('║    2 - Efetuar saque          ║')
    print('║    3 - Efetuar depósito       ║')
    print('║    4 - Efetuar transferência  ║')
    print('║    5 - Listar contas          ║')
    print('║    6 - Sair do sistema        ║')
    print('╚═══════════════════════════════╝\033[0m')
    print()

    try:
        opcao: int = int(input())
        if opcao < 1 or opcao > 6:
            raise ValueError
    except ValueError:
        print('Por favor, insira apenas números de 1 a 6!')
        sleep(1)
        return menu()

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('\033[34mSaindo do sistema.Volte sempre!')
        sleep(2)
        exit()
    else:
        print('\033[31mOpcão inválida. Por favor, tente novamente!')
        sleep(0.5)
        menu()

import re

# --------------------------------------------------------------------------------------------------------------------
# ↓ Criar contas ↓
# --------------------------------------------------------------------------------------------------------------------

def criar_conta() -> None:
    print('Informe os dados do cliente: ')

    while True:
        nome: str = input('Nome do cliente: ')
        if not re.match("^[a-zA-Z ]*$", nome):
            print('Nome inválido. Por favor, insira apenas letras e espaços!')
        else:
            break

    while True:
        email: str = input('E-mail do cliente: ')
        if not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            print('E-mail inválido. Por favor, insira um e-mail válido.')
        else:
            break

    while True:
        cpf: str = input('CPF do cliente: ')
        if not re.match("^\d{11}$", cpf):
            print('CPF inválido. Por favor, insira um CPF com 11 dígitos sem pontos ou traços!')
        else:
            break

    from datetime import datetime

    while True:
        data_nascimento: str = input('Data de nascimento do cliente (DDMMAAAA): ')
        if data_nascimento.isdigit() and len(data_nascimento) == 8:  # Verifica se a entrada é um número de 8 dígitos
            data_nascimento = data_nascimento[:2] + '/' + data_nascimento[2:4] + '/' + data_nascimento[
                                                                                       4:]  # Adiciona as barras
            try:
                datetime.strptime(data_nascimento, '%d/%m/%Y')  # Tenta converter a ‘string’ em uma data
                break
            except ValueError:
                print('Data de nascimento inválida. Por favor, insira uma data no formato DDMMAAAA!')
        else:
            print('Entrada inválida. Por favor, insira apenas números no formato DDMMAAAA!')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com sucesso!')
    print('Dados da conta: ')
    print('--------------------------------')
    print(conta)
    sleep(2)
    menu()

# --------------------------------------------------------------------------------------------------------------------
# ↓ Saque ↓
# --------------------------------------------------------------------------------------------------------------------

def efetuar_saque() -> None:
    if len(contas) > 0:
        while True:
            try:
                numero: int = int(input('Informe o número da sua conta: '))
                break
            except ValueError:
                print('Entrada inválida. Por favor, insira apenas números para a conta!')

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            while True:
                try:
                    valor: float = float(input('Informe o valor do saque: '))
                    break
                except ValueError:
                    print('Entrada inválida. Por favor, insira apenas números para o valor do saque!')

            conta.sacar(valor)
        else:
            print(f'\033[31mNão foi encontrada a conta com número {numero}!')
    else:
        print('\033[31mAinda não existem contas cadastradas!')
    sleep(2)
    menu()

# --------------------------------------------------------------------------------------------------------------------
# ↓ Depósito ↓
# --------------------------------------------------------------------------------------------------------------------

def efetuar_deposito() -> None:
    if len(contas) > 0:
        while True:
            try:
                numero: int = int(input('Informe o número da sua conta: '))
                break
            except ValueError:
                print('Entrada inválida. Por favor, insira apenas números para a conta.')

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            while True:
                try:
                    valor: float = float(input('Informe o valor do depósito: '))
                    break
                except ValueError:
                    print('Entrada inválida. Por favor, insira apenas números para o valor do depósito.')

            conta.depositar(valor)
        else:
            print(f'\033[31mNenhuma conta encontrada com o número {numero}. Por favor, tente novamente.\033[0m')
    else:
        print('\033[31mNenhuma conta registrada. Por favor, crie uma conta.\033[0m')
    sleep(1)
    menu()

# --------------------------------------------------------------------------------------------------------------------
# ↓ Transferência ↓
# --------------------------------------------------------------------------------------------------------------------

def efetuar_transferencia() -> None:
    if len(contas) > 0:
        try:
            numero_o: int = int(input('Informe o número da sua conta: '))
        except ValueError:
            print('Por favor, insira apenas números para a conta.')
            return

        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            while True:
                try:
                    numero_d: int = int(input('Informe o número da conta destino: '))
                except ValueError:
                    print('Por favor, insira apenas números para a conta.')
                    return

                if numero_o == numero_d:
                    print('Você não pode transferir para a mesma conta! Por favor, tente novamente.')
                else:
                    conta_d: Conta = buscar_conta_por_numero(numero_d)

                    if conta_d:
                        try:
                            valor: float = float(input('Informe o valor da transferência: '))
                        except ValueError:
                            print('Por favor, insira apenas números para o valor da transferência.')
                            return

                        conta_o.transferir(conta_d, valor)
                        break
                    else:
                        print(f'A conta destino com número {numero_d} não foi encontrada.')
        else:
            print(f'A sua conta com número {numero_o} não foi encontrada.')
    else:
        print('\033[31mAinda não existem contas cadastradas.')
    sleep(2)
    menu()

# --------------------------------------------------------------------------------------------------------------------
# ↓ listar contas ↓
# --------------------------------------------------------------------------------------------------------------------

def listar_contas() -> None:
    if len(contas) > 0:
        print('\033[36m╔══════════════════════════════╗')
        print('║      Listagem de contas      ║')
        print('╚══════════════════════════════╝\033[0m')

        for conta in contas:
            print(conta)
            print('--------------------------------')
            sleep(1)
    else:
        print('\033[31mNenhuma conta registrada. Por favor, crie uma conta.\033[0m')
    sleep(1)
    menu()

def buscar_conta_por_numero(numero: int) -> None:
     c: Conta = None

     if len(contas) > 0:
         for conta in contas:
             if conta.numero == numero:
                 c = conta
     return c

if __name__ == '__main__':
     main()