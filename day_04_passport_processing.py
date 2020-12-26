"""
Advent of Code 2020: Day 4. Passport Processing
@author: @SantiMontiel
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -- Data import

import os

fp = open('day_04_input.txt', 'r')

lista = []
line = fp.readline()

while line:
    lista.append(line.strip())
    line = fp.readline()

fp.close()

# -- Parte 1
passport = []
id = {}