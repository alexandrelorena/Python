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

    opcao: int = int(input())

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
        print('\033[31mOpcão inválida. Por favor, tente novamente.')
        sleep(0.5)
        menu()

def criar_conta() -> None:
     print('Informe os dados do cliente: ')

     nome: str = input('Nome do cliente: ')
     email: str = input('E-mail do cliente: ')
     cpf: str = input('CPF do cliente: ')
     data_nascimento: str = input('Data de nascimento do cliente: ')

     cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

     conta: Conta = Conta(cliente)

     contas.append(conta)

     print('Conta criada com sucesso!')
     print('Dados da conta: ')
     print('----------------')
     print(conta)
     sleep(2)
     menu()

def efetuar_saque() -> None:
     if len(contas) > 0:
        numero: int = int(input('Informe o n úmero da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque '))

            conta.sacar(valor)
        else:
            print(f'\033[31mNenhuma conta encontrada com o número {numero}. Por favor, tente novamente.\033[0m')
            sleep(1)
            menu()
     else:
        print('\033[31mNenhuma conta registrada. Por favor, crie uma conta.\033[0m')
        sleep(1)
        menu()

def efetuar_deposito() -> None:
     if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do depósito: '))

            conta.depositar(valor)
        else:
            print(f'\033[31mNenhuma conta encontrada com o número {numero}. Por favor, tente novamente.\033[0m')
     else:
        print('\033[31mNenhuma conta registrada. Por favor, crie uma conta.\033[0m')
     sleep(1)
     menu()

def efetuar_transferencia() -> None:
     if len(contas) > 0:
         numero_o: int = int(input('Por favor, informe o número da sua conta: '))

         conta_o: Conta = buscar_conta_por_numero(numero_o)

         if conta_o:
             numero_d: int = int(input('Por favor, informe o número da conta destino: '))

             conta_d: Conta = buscar_conta_por_numero(numero_d)

             if conta_d:
                 valor: float = float(input('Por favor, informe o valor da transferência: '))

                 conta_o.transferir(conta_d, valor)
             else:
                 print(f'\033[31mA conta destino com o número {numero_d} não foi encontrada\033[0m')
         else:
             print(f'\033[31mA sua conta com o número {numero_o} não foi encontrada\033[0m')
     else:
        print('\033[31mNenhuma conta registrada. Por favor, crie uma conta.\033[0m')
     sleep(1)
     menu()

def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas')

        for conta in contas:
            print(conta)
            print('----------------')
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