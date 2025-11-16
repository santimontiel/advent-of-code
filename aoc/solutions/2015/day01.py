"""Solution for Advent of Code 2015 Day 01."""

def part1(input_data: list[str]) -> int:
    puzzle = input_data[0]
    return puzzle.count("(") - puzzle.count(")")

def part2(input_data: list[str]) -> int:
    puzzle = input_data[0]
    for i in range(len(puzzle)):
        if puzzle[:i].count("(") - puzzle[:i].count(")") == -1:
            return i
    
