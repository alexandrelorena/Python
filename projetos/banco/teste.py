#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
teste

"""

from models.cliente import Cliente
from models.conta import Conta

felicity: Cliente = Cliente('Fwlicity Jones', 'felicity@gmail.com', '123.456.789-00', '01/01/2000')
angelina: Cliente = Cliente('Angelina Jolie', 'angelina@gmail.com', '234.567.890-00', '01/08/1987')

# conta_felicity: Conta = Conta(felicity)
# conta_angelina: Conta = Conta(angelina)
#
# print(conta_felicity)
# print(conta_angelina)

contaf: Conta = Conta(felicity)
contaa: Conta = Conta(angelina)

# print(contaf)
# print(contaa)