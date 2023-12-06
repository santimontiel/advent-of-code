from typing import List
from utils import summary
from tqdm.auto import tqdm


def read_input(file_path: str) -> List[str]:
    with open(file_path, "r") as fin:
        return [line.strip() for line in fin.readlines()]


def compare_range(guess, dict) -> int:

    for d, s, l in dict:
        if guess >= s and guess <= s + l:
            guess = d + (guess - s)
            return guess
    else:
        return guess


@summary
def part_1(data: List[str]) -> int:

    DICTS = {}

    # Obtain initial seeds.
    seeds = list(map(int, data[0].split(":")[1].lstrip().split(" ")))

    chunk, chunks = [], []
    for line in data[2:]:
        if line == "":
            chunks.append(chunk)
            chunk = []
        else:
            chunk.append(line)
    chunks.append(chunk)

    for i, chunk in enumerate(chunks):
        for j, line in enumerate(chunk):
            if j == 0:
                DICTS[i] = list()
            else:
                dst, src, length = list(map(int, line.split(" ")))
                DICTS[i].append([dst, src, length])
        
    guesses = []
    for seed in tqdm(seeds):
        guess = seed
        for i in range(0, len(DICTS)):
            guess = compare_range(guess, DICTS[i])
        guesses.append(guess)
    
    return min(guesses)


@summary
def part_2(data: List[str]) -> int:
    
    DICTS = {}

    # Obtain initial seeds.
    seeds = list(map(int, data[0].split(":")[1].lstrip().split(" ")))
    seeds = [seeds[i:i+2] for i in range(0, len(seeds), 2)]

    chunk, chunks = [], []
    for line in data[2:]:
        if line == "":
            chunks.append(chunk)
            chunk = []
        else:
            chunk.append(line)
    chunks.append(chunk)

    for i, chunk in enumerate(chunks):
        for j, line in enumerate(chunk):
            if j == 0:
                DICTS[i] = list()
            else:
                dst, src, length = list(map(int, line.split(" ")))
                DICTS[i].append([dst, src, length])
        
    guesses = []
    for pair in tqdm(seeds):
        for seed in tqdm(range(pair[0], pair[0] + pair[1] + 1)):
            guess = seed
            for i in range(0, len(DICTS)):
                guess = compare_range(guess, DICTS[i])
            guesses.append(guess)
    
    return min(guesses)


def main() -> None:
    data = read_input("../inputs/day_05.txt")
    part_1(data)
    part_2(data)

if __name__ == "__main__":
    main()