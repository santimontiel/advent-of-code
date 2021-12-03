""" Advent of Code 2021. Day 1: Sonar Sweep
__author__: Santiago Montiel Marín
"""

from typing import List

def parse_text(raw_puzzle: str) -> List[int]:
    with open(raw_puzzle) as f:
        text = f.readlines()
        clean_puzzle = []
        for line in text:
            clean_puzzle.append(int(line))
    return clean_puzzle

def part1(puzzle: List[int]) -> int:
    """Part 1. How many measurements are larger than the previous
    measurement?

    Args:
        - puzzle: List[int]. List that contains the measurements.

    Return:
        - counter: int. Number of measurements larger than the
            	previous one.
    """

    # Initialize previous value as maximum of the list.
    prev = 0
    for n in puzzle:
        if n > prev:
            prev = n

    # Iterate over the list to check higher measurements.
    counter = 0
    for n in puzzle:
        if n > prev:
            counter += 1
        prev = n
    return counter

def part1_singleline(puzzle: List[int]) -> int:
    return len([line[i] > line[i] for i, line in enumerate(puzzle)])

def part2(puzzle: List[int]) -> int:
    """Part 2. Count the number of times the sum of measurements in
    this sliding window increases from the previous sum. Consider 
    sums of a three-measurement sliding window. How many sums are 
    larger than the previous sum?

    Args:
        - puzzle: List[int]. List that contains the measurements.

    Return:
        - counter: int. Number of measurements windows larger than
                the	previous one.
    """
    # Initialize the previous value as maximum (infinite).
    prev = float('inf')

    # Iterate to check higher measurement groups.
    counter = 0
    for (idx, n) in enumerate(puzzle):
        if (idx == len(puzzle)-2):
            return counter
        else:
            s = puzzle[idx] + puzzle[idx+1] + puzzle[idx+2]
            if (s > prev):
                counter += 1
            prev = s

def main(args=None):
    puzzle = parse_text("input01.txt")
    print(f"Answer to question 1 is: {part1(puzzle)}")
    print(f"Answer to question 2 is: {part2(puzzle)}")

if __name__ == "__main__":
    main()