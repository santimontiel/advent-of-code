""" Advent of Code 2021. Day 3: Binary Diagnostic
__author__: Santiago Montiel Marín
"""

import doctest
from typing import List

def parse_text(raw_puzzle: str) -> List[int]:
    with open(raw_puzzle) as f:
        text = f.readlines()
        clean_puzzle = []
        for line in text:
            clean_puzzle.append(line.strip())
    return clean_puzzle

def bin2dec(binary: str) -> int:
    length = len(binary)
    decimal = 0
    for (idx, char) in enumerate(binary):
        decimal += int(char) * 2**(length-idx-1)
    return decimal

def mcv_filter(mcv, c, i):
    if c == mcv[i]:
        return True

def part1(puzzle: List[str]) -> int:
    """
    Test:
        >>> part1(["00100", "11110", "10110", "10111", "10101", \
            "01111", "00111", "11100", "10000", "11001", "00010", \
            "01010"])
        198
    """
    length = len(puzzle[0])
    counter = [0 for i in range(length)]
    for line in puzzle:
        for (idx, char) in enumerate(line):
            counter[idx] += 1 if char == "1" else 0
    elem = len(puzzle)
    mcv = ["1" if counter[idx] > int(elem/2) else "0" for (idx, el) in enumerate(counter)]
    epsilon_bin, gamma_bin = "", ""
    for n in mcv:
        if n == "1": epsilon_bin, gamma_bin = epsilon_bin + "1", gamma_bin + "0"
        else:        epsilon_bin, gamma_bin = epsilon_bin + "0", gamma_bin + "1"
    epsilon_dec = bin2dec(epsilon_bin)
    gamma_dec = bin2dec(gamma_bin)
    return epsilon_dec * gamma_dec

def part2(puzzle: List[str]) -> int:
    """
    Test:
        >>> part2(["00100", "11110", "10110", "10111", "10101", \
            "01111", "00111", "11100", "10000", "11001", "00010", \
            "01010"])
        230
    """
    length = len(puzzle[0])
    
    # Key 1
    it = 0
    puzzle_1 = puzzle.copy()
    while(len(puzzle_1)) > 1:

        # Count incidences
        counter = [0 for i in range(length)]
        for line in puzzle_1:
            for (idx, char) in enumerate(line):
                counter[idx] += 1 if char == "1" else 0
        elem = len(puzzle_1)
        
        # From incidences, mcv:
        mcv = ["1" if counter[idx] >= elem/2 else "0" for (idx, el) in enumerate(counter)]
        #lcv = ["0" if mcv[idx] == "1" else 1 for (idx, el) in enumerate(mcv)]

        # La chicha buena
        to_pop = []
        for (idx, line) in enumerate(puzzle_1):
            if mcv[it] != line[it]: to_pop.append(idx)
        to_pop = list(list(set(to_pop)).__reversed__())

        for el in to_pop:
            puzzle_1.pop(el)

        # Increase iteration counter
        it += 1
    key1 = puzzle_1[0]

    # Key 2
    it = 0
    puzzle_2 = puzzle.copy()
    while(len(puzzle_2)) > 1:

        # Count incidences
        counter = [0 for i in range(length)]
        for line in puzzle_2:
            for (idx, char) in enumerate(line):
                counter[idx] += 1 if char == "1" else 0
        elem = len(puzzle_2)
        
        # From incidences, mcv:
        mcv = ["1" if counter[idx] >= elem/2 else "0" for (idx, el) in enumerate(counter)]
        lcv = ["0" if mcv[idx] == "1" else "1" for (idx, el) in enumerate(mcv)]

        # La chicha viene acá
        to_pop = []
        for (idx, line) in enumerate(puzzle_2):
            if lcv[it] != line[it]: to_pop.append(idx)
        to_pop = list(list(set(to_pop)).__reversed__())

        for el in to_pop:
            puzzle_2.pop(el)

        # Increase iteration counter
        it += 1  
    key2 = puzzle_2[0]
    return bin2dec(key1) * bin2dec(key2)

def main(args=None):
    doctest.testmod(verbose=True)
    puzzle = parse_text("input03.txt")

    test = ["00100", "11110", "10110", "10111", "10101", \
            "01111", "00111", "11100", "10000", "11001", "00010", \
            "01010"]

    print(f"Answer to question 1 is: {part1(puzzle)}")
    print(f"Answer to question 2 is: {part2(puzzle)}")

if __name__ == "__main__":
    main()