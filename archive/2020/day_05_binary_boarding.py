"""
Advent of Code 2020: Day 5. Binary boarding.
@author: @SantiMontiel
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -- SEARCH ID FUNCTION

def look_for_id(s):
    row_code = s[:7]
    col_code = s[7:]

    # - Row decodification
    r_bit, r_min, r_max = 1, 0, 127
    for bit in row_code:
        if bit == "B":
            r_min = r_min + 2**(7-r_bit)
        elif bit == "F":
            r_max = r_max - 2**(7-r_bit)
        r_bit += 1

    row = r_max

    # - Column decodification
    c_bit, c_min, c_max = 1, 0, 7
    for bit in col_code:
        if bit == "R":
            c_min = c_min + 2**(3-c_bit)
        elif bit == "L":
            c_max = c_max - 2**(3-c_bit)
        c_bit += 1
    
    col = c_max

    # - Seat ID
    seat_id = row * 8 + col

    return seat_id

# -- DATA IMPORT

fp = open('day_05_input.txt', 'r')

text = []
line = fp.readline()

while line:
    text.append(line.strip())
    line = fp.readline()

print("Datas are imported successfully!")

# -- PART 1

id_all = []
for i in range(len(text)):
    id_i = look_for_id(text[i])
    id_all.append(id_i)

id_max = max(id_all)

print("PART 1. The highest id is: " + str(id_max))

# -- PART 2
for i in range(min(id_all), max(id_all)):
    if (i not in id_all):
        print ("PART 2. Your seat id is: " + str(i))
    
    

