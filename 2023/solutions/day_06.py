import re
from typing import List
from math import prod
from utils import summary


def read_input(file_path: str) -> List[str]:
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]


@summary
def part_1(data: List[str]) -> int:

    times = list(map(int, re.findall(r"\d+", data[0])))
    distances = list(map(int, re.findall(r"\d+", data[1])))

    records = []
    for time, distance in zip(times, distances):
        records.append(len(list(filter(lambda x: x > distance, [t * (time-t) for t in range(0, time+1)]))))
    return prod(records)

@summary
def part_2(data: List[str]) -> int:
    
    time = int("".join(re.findall(r"\d+", data[0])))
    distance = int("".join(re.findall(r"\d+", data[1])))

    return len(list(filter(lambda x: x > distance, [t * (time-t) for t in range(0, time+1)])))


def main():
    data = read_input("../inputs/day_06.txt")
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
