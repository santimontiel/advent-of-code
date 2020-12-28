"""
Advent of Code 2020: Day 6. Custom customs.
@author: @SantiMontiel
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# -- DATA IMPORT
# """"
fp = open('day_06_input.txt', 'r')

text = []
line = fp.readline()

while line:
    text.append(line.strip())
    line = fp.readline()

print("Datas are imported successfully!\n")
# """"

# text = ["abc", "", "a", "b", "c", "", "ab", "ac", "", "a", "a", "a", "a", "", "b"]
# text = ["meqnof", "vxwhzpmqo", "jno", "bkoliycr", "", "u", "u"]
# print(text)

# -- PART 1
diff_letters, num_letters_by_group = [], []

for i in text:
    if(len(i) > 0):
        for letter in i:
            if (letter not in diff_letters):
                diff_letters.append(letter)
    else:
        num_letters_by_group.append(len(diff_letters))
        diff_letters = []

# Last line is not empty, adding last group
num_letters_by_group.append(len(diff_letters))

print(str(num_letters_by_group) + "\n")
print(str(sum(num_letters_by_group)) + "\n")

# -- PART 2
cnt = 0
uni_letters, uni_letters_by_group = [], []

for i in text:
    if ((len(i) > 0) and (cnt == 0)):
        for letter in i:
            uni_letters.append(letter)  
        cnt += 1
    elif ((len(i) > 0) and (cnt != 0)):
        for letter in uni_letters:
            if (letter not in i):
                uni_letters.remove(letter)
        cnt += 1
    else:
        uni_letters_by_group.append(len(uni_letters))
        uni_letters = []
        cnt = 0

# Last line is not empty, adding last group
uni_letters_by_group.append(len(uni_letters))

print(uni_letters_by_group)
print(sum(uni_letters_by_group))
