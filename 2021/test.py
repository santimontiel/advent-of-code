from typing import List

def parse_text(raw_puzzle: str) -> List[int]:
    with open(raw_puzzle) as f:
        text = f.readlines()
        clean_puzzle = []
        for line in text:
            clean_puzzle.append(int(line))
    return clean_puzzle

def main(args=None):
    puzzle = parse_text("input01.txt")
    h = map(sum, zip(puzzle[:], puzzle[1:], puzzle[2:]))
    print(list(zip(puzzle[:], puzzle[1:], puzzle[2:])))
    # print(list(h))

if __name__ == "__main__":
    main()