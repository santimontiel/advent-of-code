from typing import List, Tuple
from utils import summary
import re


def read_input(file_path: str) -> List[int]:
    with open(file_path, "r") as fin:
        return [line.strip() for line in fin.readlines()]
    

@summary
def part_1(data: List[int]) -> int:

    points = 0
    for line in data:

        _, game = line.split(":")
        mn, wn = game.split("|")

        mn, wn = list(map(int, re.findall(r"\d+", mn))), list(map(int, re.findall(r"\d+", wn))) 
        swn = sum(list(map(lambda x: x in wn, mn)))
        points += 2 ** (swn - 1) if swn > 0 else 0

    return points


@summary
def part_2(data: List[int]) -> int:

    copies = {f"{game_id+1}": 1 for game_id in range(0, len(data))}

    for line in data:

        metadata, game = line.split(":")
        game_id = int(re.findall(r"\d+", metadata)[0])
        mn, wn = game.split("|")

        mn, wn = list(map(int, re.findall(r"\d+", mn))), list(map(int, re.findall(r"\d+", wn))) 
        swn = sum(list(map(lambda x: x in wn, mn)))
        for i in range(game_id + 1, game_id + swn + 1):
            copies[f"{i}"] += copies[f"{game_id}"]

    return sum(copies.values())


def main():
    data = read_input("../inputs/day_04.txt")
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()