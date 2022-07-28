""" Advent of Code 2021. Day 5: Hydrothermal Venture
__author__: Santiago Montiel Marín
"""

from typing import List

def parse_text(raw: str) -> List[int]:
    with open(raw) as f:
        t = f.readlines()
        clean = []
        for l in t:
            tl = l.strip().replace(' -> ', ',').split(',')
            nl = [int(el) for el in tl]
            nl[1], nl[2] = nl[2], nl[1] #x1,x2,y1,y2
            if nl[0] == nl[1]:      nl.append('ver')
            elif nl[2] == nl[3]:    nl.append('hor')
            else:                   nl.append('diag')
            clean.append(nl)
    return clean

def part1(puzzle: List[int]) -> int:

    # Grid building
    x_max, y_max = 0, 0
    for el in puzzle:
        if max(el[0], el[1]) > x_max:
            x_max = max(el[0], el[1])
        if max(el[2], el[3]) > y_max:
            y_max = max(el[2], el[3])
    grid = [[0 for i in range(x_max+1)] for j in range(y_max+1)]
    # print(f"Size of grid is: X = {x_max}, Y = {y_max}")

    # Painting the grid
    for (l, line) in enumerate(puzzle):

        # print(f"\n-- Line {l} -- {line} --")
        to_paint = []

        # Processing horizontal lines
        if line[4] == "hor":
            if line[1] < line[0]:
                line[1], line[0] = line[0], line[1]
            to_paint = list(range(line[0], line[1]+1))
            row = line[3]
            for el in to_paint:
                grid[row][el] += 1

        # Processing vertical lines
        elif line[4] == "ver":
            if line[3] < line[2]:
                line[3], line[2] = line[2], line[3]
            to_paint = list(range(line[2], line[3]+1))
            col = line[0]
            for el in to_paint:
                grid[el][col] += 1
        
        # Nothing to do with diagonal lines
        else:
            pass

    # print(grid)
    # Count elements higher than 1
    acum = 0
    for row in grid:
        for el in row:
            if el > 1:
                acum += 1
    
    return acum
    

def part2(puzzle: List[int]) -> int:
    
    # Grid building
    x_max, y_max = 0, 0
    for el in puzzle:
        if max(el[0], el[1]) > x_max:
            x_max = max(el[0], el[1])
        if max(el[2], el[3]) > y_max:
            y_max = max(el[2], el[3])
    grid = [[0 for i in range(x_max+1)] for j in range(y_max+1)]
    # print(f"Size of grid is: X = {x_max}, Y = {y_max}")

    # Painting the grid
    for (l, line) in enumerate(puzzle):

        # print(f"\n-- Line {l} -- {line} --")
        to_paint = []

        # Processing horizontal lines
        if line[4] == "hor":
            if line[1] < line[0]:
                line[1], line[0] = line[0], line[1]
            to_paint = list(range(line[0], line[1]+1))
            row = line[3]
            for el in to_paint:
                grid[row][el] += 1

        # Processing vertical lines
        elif line[4] == "ver":
            if line[3] < line[2]:
                line[3], line[2] = line[2], line[3]
            to_paint = list(range(line[2], line[3]+1))
            col = line[0]
            for el in to_paint:
                grid[el][col] += 1
        
        # Nothing to do with diagonal lines
        elif line[4] == "diag":
            x1, x2, y1, y2, dir = line
            if (x1 < x2 and y1 < y2):
                inc_x = list(range(x1,x2+1))
                inc_y = list(range(y1,y2+1))
                to_paint = list(zip(inc_x, inc_y))
                print(f"** 1 ** {line} ** {to_paint} **")

            elif (x1 < x2 and y1 > y2):
                inc_x = list(range(x1,x2+1))
                inc_y = list(range(y1,y2-1,-1))
                to_paint = list(zip(inc_x, inc_y))
                print(f"** 2 ** {line} ** {to_paint} **")

            elif (x1 > x2 and y1 < y2):
                inc_x = list(range(x1,x2-1,-1))
                inc_y = list(range(y1,y2+1))
                to_paint = list(zip(inc_x, inc_y))
                print(f"** 3 ** {line} ** {to_paint} **")

            elif (x1 > x2 and y1 > y2):
                inc_x = list(range(x1,x2-1,-1))
                inc_y = list(range(y1,y2-1,-1))
                to_paint = list(zip(inc_x, inc_y))
                print(f"** 4 ** {line} ** {to_paint} **")

            for ex, ey in to_paint:
                grid[ex][ey] += 1            

    # print(grid)
    # Count elements higher than 1
    acum = 0
    for row in grid:
        for el in row:
            if el > 1:
                acum += 1
    
    for el in grid:
        print(el)

    return acum

def main(args=None):
    puzzle = parse_text("input05.txt")
    print(f"Answer to question 1 is: {part1(puzzle)}")
    print(f"Answer to question 2 is: {part2(puzzle)}")

if __name__ == "__main__":
    main()