"""
Advent of Code 2020: Day 2. Password Philosophy
@author: @SantiMontiel
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

fp = open('day_02_input.txt', 'r')

min = []
max = []
let = []
pwd = []
lista = []
line = fp.readline()
num_valid = 0

while line:
    lista.append(line.strip())
    line = fp.readline()

fp.close()

# -- PART 1
print("Parte 1:")
for i in range(0, len(lista)):
    # Separando la cadena en partes interesantes
    minmax, let_i, pwd_i = lista[i].split(' ')
    pwd.append(pwd_i)
    min_i, max_i = minmax.split('-')
    min.append(int(min_i))
    max.append(int(max_i))
    let_i = let_i.strip(':')
    let.append(let_i)

    # Viendo si la pass es correcta
    num = pwd[i].count(let[i])
    if (num >= min[i] and num <= max[i]):
        #print("La pass " + str(i) + "es correcta.")
        num_valid += 1

print("Hay " + str(num_valid) + " pass correctas en la parte 1")

# -- PARTE 2
num_valid_b = 0

print("Parte 2:")
for i in range(0, len(lista)):
    x = 0
    if(pwd[i][max[i]-1] == let[i]):
        x += 1
    if(pwd[i][min[i]-1] == let[i]):
        x += 1
    if(x == 1):
        num_valid_b += 1
        #print("La pass " + str(i) + "es correcta.")

print("Hay " + str(num_valid_b) + " pass correctas en la parte 2")

