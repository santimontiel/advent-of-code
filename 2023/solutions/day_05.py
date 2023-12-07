from typing import List
from utils import summary


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
    for seed in seeds:
        guess = seed
        for i in range(0, len(DICTS)):
            guess = compare_range(guess, DICTS[i])
        guesses.append(guess)
    
    return min(guesses)



# First time I approach part 2 with total refactoring: mapping in
# reverse technique here, instead of brute force.
def read_input2(file_path: str) -> List[str]:
    with open(file_path, "r") as fin:
        return fin.read().split("\n\n")


def mapping_in_reverse(n: int, ranges: List[int]):
    for dst, src, length in ranges:
        if n >= dst and n < dst + length:
            return src + (n - dst)
    else:
        return n
    

@summary
def part_2(data: List[str]) -> int:
    
    ranges = []
    chunks = [line.split("\n")[1:] for line in data[1:]]
    for chunk in chunks:
        this_range = []
        for r in chunk:
            this_range.append(list(map(int, r.split(" "))))
        ranges.append(this_range)

    seeds = list(map(int, data[0].split(":")[1].lstrip().split(" ")))
    seeds = [seeds[i:i+2] for i in range(0, len(seeds), 2)]
    seeds = sorted(seeds, key=lambda x: x[0])

    min_location = 0
    location = -1
    while min_location == 0:
        
        location += 1
        n = location
        
        for r in ranges[::-1]:
            n = mapping_in_reverse(n, r)
        
        for src, length in seeds:
            if n >= src and n < src + length:
                min_location = location

    return min_location


def main() -> None:
    data = read_input("../inputs/day_05.txt")
    part_1(data)
    data = read_input2("../inputs/day_05.txt")
    part_2(data)

if __name__ == "__main__":
    main()