"""Solution for Advent of Code 2025 Day 06."""
from functools import reduce


def part1(input_data: list[str]) -> int:
    # Parse input data and transpose list of lists.
    all_numbers = []
    for line in input_data:
        all_numbers.append([num for num in line.split(" ") if num != ""])
    all_numbers_T = [list(x) for x in zip(*all_numbers)]

    OPS = {"+": lambda x, y: x + y, "*": lambda x, y: x * y}

    result = 0
    for prob in all_numbers_T:
        numbers = [int(x) for x in prob[:-1]]
        result += reduce(OPS[prob[-1]], numbers)

    return result


def part2(input_data: list[str]) -> int:
    # We go for a custom logic for vertical parsing.
    STARTS = [i for i, char in enumerate(input_data[-1]) if char in ["+", "*"]]
    ENDS = [i - 1 for i in STARTS] + [len(input_data[0])]
    HEIGHT = len(input_data) - 1

    rearranged_numbers = []
    windows = zip(STARTS, ENDS[1:])
    for start, end in windows:
        this_sequence = []
        for idx in range(start, end):
            this_number = ""
            for idy in range(HEIGHT):
                if input_data[idy][idx] != " ":
                    this_number += input_data[idy][idx]
            this_sequence.append(int(this_number))

        this_sequence.append(input_data[HEIGHT][start])
        rearranged_numbers.append(this_sequence)

    # Once numbers are rearranged, solve like Part 1.
    OPS = {"+": lambda x, y: x + y, "*": lambda x, y: x * y}

    result = 0
    for prob in rearranged_numbers:
        numbers = [int(x) for x in prob[:-1]]
        result += reduce(OPS[prob[-1]], numbers)

    return result
