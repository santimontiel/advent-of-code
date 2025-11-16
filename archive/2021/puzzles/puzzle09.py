""" Advent of Code 2021. Day X:
__author__: Santiago Montiel Marín
"""

from typing import List

def parse_text(raw_puzzle: str) -> List[int]:
    with open(raw_puzzle) as f:
        text = f.readlines()
        clean_puzzle = []
        for line in text:
            clean_puzzle.append([int(char) for char in line.strip()])
    return clean_puzzle

def part1(puzzle: List[int]) -> int:
    # neighbors = [
    # [i-1][j], # Left
    # [i+1][j], # Right
    # [i][j-1], # Up
    # [i][j+1], # Down
    # ]
    
    def evaluate(point, map):
        neighbours = 0
        if point[0] != 0:
            pass
            # Neighbour at left

    def check_up(puzzle, x, y):
        return puzzle[x][y] < puzzle[x][y-1]
    def check_down(puzzle, x, y):
        return puzzle[x][y] < puzzle[x][y+1]
    def check_left(puzzle, x, y):
        return puzzle[x][y] < puzzle[x-1][y]
    def check_right(puzzle, x, y):
        return puzzle[x][y] < puzzle[x+1][y]
    
    def get_neighbours(x,y,ll,rl):
        candidates = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        to_del = []
        for (n,c) in enumerate(candidates):
            if c[0] < 0 or c[0] > ll:
                to_del.append(n)
            if c[1] < 0 or c[1] > rl:
                to_del.append(n)
        to_del = list(to_del.__reversed__())
        for i in to_del:
            candidates.pop(i)
        return candidates

    acum = 0
    LOWER_LIMIT = len(puzzle)-1
    RIGHT_LIMIT = len(puzzle[0])-1
    for (i,row) in enumerate(puzzle):
        for (j,el) in enumerate(row):
            neighbours = get_neighbours(i, j,LOWER_LIMIT, RIGHT_LIMIT)
            print(f"** Number {el} with n: {neighbours} ** R: {RIGHT_LIMIT} ** L: {LOWER_LIMIT} **")
            ltn_acum = 0
            for (nx,ny) in neighbours:
                if el < puzzle[nx][ny]:  ltn_acum += 1
            if ltn_acum == len(neighbours): acum += 1

    return acum


    # for (i, line) in enumerate(puzzle):
    #     for (j, char) in enumerate(line):
    #         neighbors = []
            

def part2(puzzle: List[int]) -> int:
    pass

def main(args=None):
    puzzle = parse_text("input09.txt")
    print(f"Answer to question 1 is: {part1(puzzle)}")
    print(f"Answer to question 2 is: {part2(puzzle)}")

if __name__ == "__main__":
    main()