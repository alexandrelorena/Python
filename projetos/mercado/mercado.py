#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Projeto — Mercado

mercado

"""

from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()

def menu() -> None:
    print('╔══════════════════════════════╗')
    print('╠════════ Bem vindo(a) ════════╣')
    print('╠════════════ Shop ════════════╣')
    print('╠══════════════════════════════╣')
    print('║  Selecione uma opção abaixo  ║')
    print('╠══════════════════════════════╣')
    print('║    1 - Cadastrar produto     ║')
    print('║    2 - Listar produtos       ║')
    print('║    3 - Comprar produtos      ║')
    print('║    4 - Visualizar carrinho   ║')
    print('║    5 - Fechar pedido         ║')
    print('║    6 - Sair do sistema       ║')
    print('╚══════════════════════════════╝')
    print()

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida!')
        sleep(1)
        menu()

def cadastrar_produto() -> None:
    print('╔══════════════════════════════╗')
    print('║       Cadastrar Produto      ║')
    print('╚══════════════════════════════╝')

    nome: str = input('Informe o nome do produto: ')

    while True:
        try:
            preco_input: str = input('Informe o preço do produto: ')

            # Substitui vírgulas por pontos
            preco_input = preco_input.replace(',', '.')

            # Verifica se o preço é um número
            if not preco_input.replace('.', '', 1).isdigit():
                raise ValueError("O preço deve ser um número.")

            preco: float = float(preco_input)

            # Verifica se o preço é maior que zero
            if preco <= 0:
                raise ValueError("O preço deve ser maior que zero.")

            break  # Sai do ‘loop’ se não houver erros
        except ValueError as ve:
            print(f'Ocorreu um erro ao cadastrar o produto: {str(ve)}')
            print('Por favor, tente novamente.')

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print('╔══════════════════════════════╗')
        print('║        Listar produtos       ║')
        print('╚══════════════════════════════╝')

        for produto in produtos:
            print(produto)
            print('--------------------')
            sleep(1)
    else:
        print('Nenhum produto encontrado.')
    sleep(2)
    menu()

def comprar_produto() -> None:
    if len(produtos) > 0:
        print('╔═ Informe o código do produto desejado ═╗')
        print('╠════════════════════════════════════════╣')
        print('╚═════════ Produtos disponíveis ═════════╝')

        for produto in produtos:
            print(produto)
            print('------------------------------------------')
            sleep(1)

        while True:
            try:
                codigo: int = int(input())
                break  # Sai do ‘loop’ se não houver erros
            except ValueError:
                print('Erro: o código do produto deve ser um número. Por favor, tente novamente.')

        produto: Produto = pega_produto_por_codigo(codigo)


        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades 1no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho!')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho!')
                sleep(2)
                menu()
        else:
            print(f'O produto com o código {codigo} não foi encontrado.')
            sleep(2)
            menu()
    else:
        print('Nenhum produto encontrado.')
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('--------------------')
                sleep(1)
    else:
        print('Carrinho vazio.')
    sleep(2)
    menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do carrinho:')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('--------------------')
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print('╔══════════════════════════════╗')
        print('╠════════ Volte sempre! ═══════╣')
        print('╚══════════════════════════════╝')

        carrinho.clear()
        sleep(2)
    else:
        print('Não há produtos no carrinho!')
    sleep(2)
    menu()

# noinspection PyTypeChecker
def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ == '__main__':
    main()
