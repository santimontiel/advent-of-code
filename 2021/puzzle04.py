""" Advent of Code 2021. Day 4: Giant Squid
__author__: Santiago Montiel Marín
"""

from typing import List

def parse_text(raw_puzzle: str) -> List[int]:
    with open(raw_puzzle) as f:
        text = f.readlines()
        numbers, *boards = text
        numbers = [int(el) for el in numbers.split(',')]
        clean_boards, acum = [], []
        for el in boards[1:]:
            if el == "\n":
                clean_boards.append(acum)
                acum = []
            else:
                el = el.strip().split()
                for n in el:
                    n = int(n)
                acum += el
        clean_boards.append(acum)
    return (numbers, clean_boards)


def part1(puzzle: List[int]) -> int:
    numbers, boards = puzzle
    
    def check_winner(numbers, boards):
        winners = [
            [ 0,  1,  2,  3,  4],
            [ 5,  6,  7,  8,  9],
            [10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19],
            [20, 21, 22, 23, 24],
            [ 0,  5, 10, 15, 20],
            [ 1,  6, 11, 16, 21],
            [ 2,  7, 12, 17, 22],
            [ 3,  8, 13, 18, 23],
            [ 4,  9, 14, 19, 24],
        ]

        indices = [[] for i in range(len(boards))]
        for number in numbers:
            for (i, board) in enumerate(boards):
                if str(number) in board:
                    indices[i].append(board.index(str(number)))
                    indices[i].sort()
            
            for (j, ind) in enumerate(indices):    
                for winner in winners:
                    acum = 0
                    for el in winner:
                        if el in ind:
                            acum += 1
                        if acum == 5:
                            print(winner)
                            return (boards[j], indices[j], number)

    ticket, indices, last = check_winner(numbers, boards)
    acum = 0
    for (i, el) in enumerate(ticket):
        if i not in indices:
            acum += int(ticket[i])
    return acum * int(last)


def part2(puzzle: List[int]) -> int:
    numbers, boards = puzzle
    
    def check_last_winner(numbers, boards):
        winners = [
            [ 0,  1,  2,  3,  4],
            [ 5,  6,  7,  8,  9],
            [10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19],
            [20, 21, 22, 23, 24],
            [ 0,  5, 10, 15, 20],
            [ 1,  6, 11, 16, 21],
            [ 2,  7, 12, 17, 22],
            [ 3,  8, 13, 18, 23],
            [ 4,  9, 14, 19, 24],
        ]

        indices = [[] for i in range(len(boards))]
        b_acum, b_ind = 0, []
        for number in numbers:
            for (i, board) in enumerate(boards):
                if str(number) in board:
                    indices[i].append(board.index(str(number)))
                    indices[i].sort()
            
            for (j, ind) in enumerate(indices):
                for winner in winners:
                    acum = 0
                    for el in winner:
                        if el in ind:
                            acum += 1
                        if acum == 5 and j not in b_ind:
                            b_acum += 1
                            b_ind.append(j)
                        if b_acum == len(boards):
                            return (boards[j], indices[j], number)

    [ticket, indices, last] = check_last_winner(numbers, boards)
    acum = 0
    for (i, el) in enumerate(ticket):
        if i not in indices:
            acum += int(ticket[i])
    return acum * int(last)

def main(args=None):
    puzzle = parse_text("input04.txt")
    print(f"Answer to question 1 is: {part1(puzzle)}")
    print(f"Answer to question 2 is: {part2(puzzle)}")

if __name__ == "__main__":
    main()