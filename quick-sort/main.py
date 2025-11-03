#! /usr/bin/env python3
import random

lista = []

for _ in range(10):
    lista.append(random.randint(0, 100))

print(lista)


def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pointer = array[0]

        lowers = [i for i in array[1:] if i <= pointer]
        highers = [i for i in array[1:] if i > pointer]

        return quickSort(lowers) + [pointer] + quickSort(highers)


print(quickSort(lista))
