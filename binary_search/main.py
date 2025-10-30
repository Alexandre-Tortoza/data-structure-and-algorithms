#! /usr/bin/env python3

"""
python 3.13.7
"""

import sys

if len(sys.argv) == 1:
    print("Você deve informar o elemento que deseja buscar")
    sys.exit()


lista = list(range(1, 11))


def binarySearch(target):
    baixo = 0  # Vamos pegar o 1 elemnto da lista
    alto = len(lista) - 1  # Vamos pegar o ultimo elemento da lista

    etapas = 0

    while baixo <= alto:
        print(f"Etapas da busca binaria: {etapas}")
        etapas = etapas + 1

        head_index = (baixo + alto) // 2  # o head vai apontar para o meio da lista
        head = lista[head_index]

        if head == target:
            return head

        if head > target:
            alto = head_index - 1

        if head < target:
            baixo = head_index + 1

    return None


print(binarySearch(int(sys.argv[1])))
