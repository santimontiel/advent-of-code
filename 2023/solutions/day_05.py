from typing import List
from utils import summary
from tqdm.auto import tqdm


def read_input(file_path: str) -> List[str]:
    with open(file_path, "r") as fin:
        return [line.strip() for line in fin.readlines()]


def compare_range(guess, dict) -> int:

    for d, s, l in dict:
        if guess in range(s, s + l + 1):
            for i, x in enumerate(range(s, s + l)):
                if guess == x:
                    guess = d + i
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

data = read_input("../inputs/day_05.txt")
part_1(data)

# data = ["50 98 2", "52 50 48"]

# data_as_int = []
# for line in data:
#     data_as_int.append([int(x) for x in line.split()])

# for line in data_as_int:
#     dst = line[0]
#     src = line[1]
#     length = line[2]

#     src_soil = list(range(src, src + length))
#     dst_soil = list(range(dst, dst + length))
#     print(list(zip(src_soil, dst_soil)))