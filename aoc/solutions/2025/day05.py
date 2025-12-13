"""Solution for Advent of Code 2025 Day 05."""
import re
from copy import deepcopy

Interval = list[int, int]

def part1(input_data: list[str]) -> int:
    
    # Parse the input.
    ranges, ingredients = [], []
    for line in input_data:
        if re.fullmatch(r"(\d+)-(\d+)", line):
            ranges.append([int(x) for x in line.split("-")])
        elif re.fullmatch(r"(\d+)", line):
            ingredients.append(int(line))

    # Iterate through the ingredients.
    fresh_ingredients = 0
    for ing in ingredients:
        for start, end in ranges:
            if start <= ing <= end:
                fresh_ingredients += 1
                break

    return fresh_ingredients


def part2(input_data: list[str]) -> int:

    def overlap(a: Interval, b: Interval) -> bool:
        return a[0] <= b[1] and b[0] <= a[1]
    
    def merge(a: Interval, b: Interval) -> Interval:
        return [min(a[0], b[0]), max(a[1], b[1])]

    def merge_batch(ivs: list[Interval]) -> Interval:
        start = min([iv[0] for iv in ivs])
        end = max([iv[1] for iv in ivs])
        return [start, end]
    
    # Parse the input.
    ranges = []
    for line in input_data:
        if re.fullmatch(r"(\d+)-(\d+)", line):
            ranges.append([int(x) for x in line.split("-")])

    # Merge overlapping intervals.
    survivors = deepcopy(ranges)
    for og_ran in ranges:
        overlaps = [overlap(og_ran, survivors[i]) for i in range(len(survivors))]
        merged = merge_batch([ran for i, ran in enumerate(survivors) if overlaps[i]])
        survivors = [ran for i, ran in enumerate(survivors) if not overlaps[i]] + [merged]

    # Sum the surviving ids (bounds are inclusive).
    ids = 0
    for start, end in survivors:
        ids += (end - start + 1)

    return ids