"""
Advent of Code 2020: Day 1. Report Repair
@author: @SantiMontiel
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# print(os.getcwd())  # Obtengo el directorio actual

fp = open('day_01_input.txt', 'r')

line = fp.readline()
lista = []

while line:
    lista.append(int(line.strip()))
    line = fp.readline()

# -- PART 1
print("PARTE 1:")
for i in range(len(lista)):
    for j in range(i, len(lista)):
        if (lista[i] + lista[j] == 2020):
            print("El número " + str(lista[i]) + " y el número " + str(lista[j]) + " suman 2020.")
            print("Su multiplicación es: " + str(lista[i]*lista[j]))


# -- PART 2
print("PARTE 2:")
for i in range(len(lista)):
    for j in range(i, len(lista)):
        for k in range(j, len(lista)):
            if (lista[i] + lista[j] + lista[k] == 2020):
                print("El número " + str(lista[i]) + ", el número " + str(lista[j]) + " y el número " + str(lista[k]) +" suman 2020.")
                print("Su multiplicación es: " + str(lista[i]*lista[j]*lista[k]))


fp.close()