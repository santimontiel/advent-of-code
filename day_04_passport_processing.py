"""
Advent of Code 2020: Day 4. Passport Processing
@author: @SantiMontiel
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -- Data import

import os

fp = open('day_04_input.txt', 'r')

# Parseo el fichero, pongo todos los datos en una única línea.
# Cada línea comienza con un espacio.

reg_i = ""
reg = []
line = fp.readline()

while line:
    
    if (len(line) > 1):
        reg_i = reg_i + " " + line[:-1]
    else:
        reg.append(reg_i)
        # print(reg_i)
        reg_i = ""
        # print("*****")
                
    line = fp.readline()    

print(len(reg))

fp.close()

# Si hay 8 parámetros -> válido y si hay 7 parámetros, pero no esta 'cid' -> válido
valido, fallo = 0, 0

for i in range(len(reg)):
    
    print(reg[i])

    if ((reg[i].count(" ") == 8) or (reg[i].count(" ") == 7 and reg[i].find("cid:") == -1)):
        valido += 1
    else:
        fallo += 1
    
    print("valido :" + str(valido) + ", falso: " + str(fallo))
    print("------------------------------------------------")
    

print("Hay " + str(valido) + " pasaportes válidos y " + str(fallo) + " pasaportes inválidos.")

