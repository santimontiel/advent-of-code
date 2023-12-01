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


def read_input(file_path: str) -> List[str]:
    with open("../inputs/day_01.txt", 'r') as fin:
        return [line.strip() for line in fin.readlines()]


# Part 1.
@summary
def part_1_orig(data: List[str]) -> int:
    only_digits = []
    for line in data:
        new_line = ""
        for char in line:
            if char.isdigit():
                new_line += char
        only_digits.append(new_line)

    results = []
    for line in only_digits:
        results.append(int(line[0]) * 10 + int(line[-1]) * 1)
    return sum(results)


# Part 2.
@summary
def part_2_orig(data: List[str]) -> int:
    DIGITS = {
        "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7",
        "8": "8", "9": "9", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    only_digits_2 = []
    for line in data:
        new_line = ""
        for i, char in enumerate(line):
            for pattern in DIGITS.keys():
                if line[i:].startswith(pattern):
                    if char.isdigit():
                        new_line += char
                    elif pattern in DIGITS.keys():
                        new_line += DIGITS[pattern]
        only_digits_2.append(new_line)

    results_2 = []
    for line in only_digits_2:
        results_2.append(int(line[0]) * 10 + int(line[-1]) * 1)
    return (sum(results_2))


# Part 1 refactored.
@summary
def part_1(data: List[str]) -> int:
    digits = [list(filter(lambda x: x.isdigit(), line)) for line in data]
    return sum([int(line[0]) * 10 + int(line[-1]) * 1 for line in digits])
    

# Part 2 refactored.
@summary
def part_2(data: List[str]) -> int:
    DIGITS = {
        "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7",
        "8": "8", "9": "9", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    def get_digit(line: str) -> str:
        for (i, c) in enumerate(line):
            for pattern in DIGITS.keys():
                if line[i:].startswith(pattern):
                    if c.isdigit():
                        print
                        return int(c)
                    elif pattern in DIGITS.keys():
                        return int(DIGITS[pattern])
        return ""
    dig = [list(map(get_digit, line.split())) for line in data]
    return sum([int(line[0]) * 10 + int(line[-1]) * 1 for line in dig])


def main(mode: str = "original"):
    
    SOLUTIONS = {
        "original": [part_1_orig, part_2_orig],
        "refined": [part_1, part_2]
    }

    data = read_input("../inputs/day_01.txt")
    res_1 = SOLUTIONS[mode][0](data)
    res_2 = SOLUTIONS[mode][1](data)


if __name__ == "__main__":
    main("original")
    main("refined")