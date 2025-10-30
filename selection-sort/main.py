#! /usr/bin/env python3

"""
Python 3.13.7
"""

import random


def getRandomList():
    lista_local = []
    for _ in range(10):
        lista_local.append(random.randint(1, 100))

    return lista_local


lista = getRandomList()

print(lista)
print("\n")


def getMenor():
    menor = lista[0]
    menor_index = 0

    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            menor_index = i

    return menor_index


def selectionSort():
    nova_lista = []

    for _ in range(len(lista)):
        menor = getMenor()
        nova_lista.append(lista.pop(menor))

    return nova_lista


print(selectionSort())
