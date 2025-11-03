#! /usr/bin/env python3

import random

lista = []

for _ in range(0, 9):
    lista.append(random.randint(0, 10))

print(lista)


def sum(lista_a_somar):
    if len(lista_a_somar) == 0:
        return 0

    item = lista.pop(0)

    total = item + sum(lista_a_somar)
    return total


print(sum(lista))
