from typing import List
import time


def summary(f):

    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print(f"Summary for {f.__name__}:")
        print(f"   >>> Result: {result}")
        print(f"   >>> Time: {((te-ts) * 1e3):.3f} ms")
        return result

    return timed


def read_input(file_path: str) -> List[int]:
    with open(file_path, "r") as fin:
        return [line.strip() for line in fin.readlines()]


@summary
def part_1(data: List[str]) -> int:

    CUBES = {
        "red": 12, 
        "green": 13,
        "blue": 14
    }

    counter = set()
    for line in data:

        metadata, game = line.split(":")
        game_id = int(metadata.split(" ")[1])

        rounds = game.split(";")
        for r in rounds:
            moves = r.lstrip().split(", ")
            for move in moves:
                q, c = move.split(" ")
                if CUBES[c] < int(q):
                    counter.add(game_id)

    return sum(list(range(0, game_id + 1))) - sum(counter)


@summary
def part_2(data: List[str]) -> int:
    
    counter = 0
    for line in data:

        cubes = {
            "red": 0, 
            "green": 0,
            "blue": 0
        }

        _, game = line.split(":")

        rounds = game.split(";")
        for r in rounds:
            moves = r.lstrip().split(", ")
            for move in moves:
                q, c = move.split(" ")
                if cubes[c] < int(q):
                    cubes[c] = int(q)

        counter += cubes["red"] * cubes["green"] * cubes["blue"]

    return counter


def main():

    data = read_input("../inputs/day_02.txt")
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
