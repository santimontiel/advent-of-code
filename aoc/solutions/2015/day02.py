"""Solution for Advent of Code 2015 Day 02."""

def part1(input_data: list[str]) -> int:
    counter = 0
    for line in input_data:
        l, w, h = map(int, line.split("x"))
        counter += (2 * l * w) + (2 * w * h) + (2 * l * h) + min(l * w, w * h, h * l)
    return counter

def part2(input_data: list[str]) -> int:
    counter = 0
    for line in input_data:
        sides = sorted(map(int, line.split("x")))
        counter += (2 * sides[0]) + (2 * sides[1]) + (sides[0] * sides[1] * sides[2])
    return counter

