#! /usr/bin/env python3
import random

lista = [random.randint(0, 100) for _ in range(15)]


def getMenor(arr):
    menorValor = arr[0]
    menorValorIndex = 0

    for i in range(len(arr)):
        if arr[i] < menorValor:
            menorValor = arr[i]
            menorValorIndex = i
    return menorValorIndex


def getMaior(arr):
    maiorValor = arr[0]
    maiorValorIndex = 0

    for i in range(len(arr)):
        if arr[i] > maiorValor:
            maiorValor = arr[i]
            maiorValorIndex = i
    return maiorValorIndex


def selectionSort(direction):
    arr = lista.copy()
    novaLista = []

    if direction == "asc":
        for _ in range(len(arr)):
            menor = getMenor(arr)
            novaLista.append(arr.pop(menor))

    elif direction == "dsc":
        for _ in range(len(arr)):
            maior = getMaior(arr)
            novaLista.append(arr.pop(maior))

    return novaLista


print("lst", lista)
print("asc", selectionSort("asc"))
print("dsc", selectionSort("dsc"))
