"""
Advent of Code 2020: Day 3. Toboggan Trajectory
@author: @SantiMontiel
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

fp = open('day_03_input.txt', 'r')

lista = []
line = fp.readline()

while line:
    lista.append(line.strip())
    line = fp.readline()

fp.close()

num_open, num_trees = 0, 0

# -- PARTE 1
print("Parte 1:")
for i in range(1, len(lista)):

    # 1. Position update
    if (i == 1):
        [X_pos, Y_pos] = [3, 1]
        # print([X_pos, Y_pos])
    else:
        [X_pos, Y_pos] = [(X_pos + 3) % 31, i]
        # print([X_pos, Y_pos])

    # 2. Check if cell is '.' or '#'
    if (lista[Y_pos][X_pos] == '#'):
        num_trees += 1
        # print("arbol = " + str(num_trees))
    elif (lista[Y_pos][X_pos] == '.'):
        num_open += 1
        # print("open = " + str(num_open))

print("Durante la trayectoria nos encontramos con " + str(num_trees) + " árboles y " + str(num_open) + " casillas abiertas.")

# -- PARTE 2

print("Parte 2:")

X_pos, Y_pos = [0, 0]
X_inc = [1, 3, 5, 7, 1]
Y_inc = [1, 1, 1, 1, 2] 
prod  = 1   

for z in range(0, len(X_inc)):

    num_open, num_trees = 0, 0
    iter = int(len(lista)/Y_inc[z])

    for i in range(1, iter):

        # 1. Position update
        if (i == 1):
            [X_pos, Y_pos] = [X_inc[z], Y_inc[z]]
        else:
            [X_pos, Y_pos] = [(X_pos + X_inc[z]) % 31, Y_inc[z]*i % 323]
            # print([X_pos, Y_pos])

        # 2. Check if cell is '.' or '#'
        if (lista[Y_pos][X_pos] == '#'):
            num_trees += 1
        elif (lista[Y_pos][X_pos] == '.'):
            num_open += 1
                
    print("Traj: (" + str(X_inc[z]) + ", " + str(Y_inc[z]) + ") -> " + str(num_trees) + " árboles")
    prod = prod * num_trees

print("El productorio de árboles es: " + str(prod))