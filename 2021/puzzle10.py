""" Advent of Code 2021. Day 10: Syntax Scoring
__author__: Santiago Montiel Marín
"""

from typing import List

def parse_text(raw_puzzle: str) -> List[int]:
    with open(raw_puzzle) as f:
        text = f.readlines()
        clean_puzzle = []
        for line in text:
            clean_puzzle.append(line.strip())
    return clean_puzzle

def part1(puzzle: List[int]) -> int:
    # s_open  = [ord('('), ord('['), ord('{'), ord('<')]
    # s_close = [ord(')'), ord(']'), ord('}'), ord('>')]
    s_open  = ['(', '[', '{', '<']
    s_close = [')', ']', '}', '>']
    count   = [0, 0, 0, 0]
    mult_f  = [3, 57, 1197, 25137]

    for line in puzzle:
        counter = [0, 0, 0, 0, 0, 0, 0, 0]
        for (i, char) in enumerate(line):
            if char in keys:
                pass

    
        

def part2(puzzle: List[int]) -> int:
    pass

def main(args=None):
    puzzle = parse_text("test10.txt")
    print(f"Answer to question 1 is: {part1(puzzle)}")
    print(f"Answer to question 2 is: {part2(puzzle)}")

if __name__ == "__main__":
    main()