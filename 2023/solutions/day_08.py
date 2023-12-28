from typing import Dict, List, Any
from utils import summary
from math import lcm


def read_input(file_name: str) -> List[str]:
    return [line.strip() for line in open(file_name, "r").readlines()]


@summary
def part_1(data: List[str]) -> int:

    sequence = data[0]

    LEFTS, RIGHTS = {}, {}
    for line in data[2:]:
        k, l, r = (
            line
                .replace(" ", "")
                .replace("=(", ",")[:-1]
                .split(",")
        )
        LEFTS[k], RIGHTS[k] = l, r

    i, key = 0, "AAA"
    while True:
        move = sequence[i % len(sequence)]
        key = LEFTS[key] if move == "L" else RIGHTS[key]
        i += 1
        if key == "ZZZ":
            break
        
    return i


def lookup_table(initial_key, move, letter, LEFTS, RIGHTS):

    i = 0
    key = initial_key
    while True:
        key = LEFTS[key] if move == "L" else RIGHTS[key]
        if key.endswith(letter):
            print(key)
            break
        i += 1
        if i % 10_000_000 == 0:
            print(i)
        
    return key


@summary
def part_2(data: List[str]) -> int:
    
    KEYS = []
    LEFTS, RIGHTS = {}, {}
    for line in data[2:]:
        k, l, r = (
            line
                .replace(" ", "")
                .replace("=(", ",")[:-1]
                .split(",")
        )
        KEYS.append(k)
        LEFTS[k], RIGHTS[k] = l, r

    starting_nodes = [k for k in KEYS if k.endswith("A")]

    steps, sequence = [], data[0]

    for node in starting_nodes:
        these_steps = 0
        while True:
            move = sequence[these_steps % len(sequence)]
            node = LEFTS[node] if move == "L" else RIGHTS[node]
            these_steps += 1
            if node.endswith("Z"):
                break
            if these_steps % 10_000_000 == 0:
                print(these_steps)
        steps.append(these_steps)

    return lcm(*steps)


def main():
    data = read_input("../inputs/day_08.txt")
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()