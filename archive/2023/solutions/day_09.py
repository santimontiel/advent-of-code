from typing import List
from utils import summary


def read_input(file_name: str) -> List[str]:
    with open(file_name, "r") as fin:
        return [list(map(int, line.strip().split())) for line in fin.readlines()]
    

@summary
def part_1(data: List[List[str]]) -> int:

    accum = 0
    for line in data:

        l = line
        cnt = l[-1]

        while True:
        
            if all(x == 0 for x in l):
                break
        
            l = [b - a for a, b in zip(l[:-1], l[1:])]
            cnt += l[-1]
        
        accum += cnt        

    return accum


@summary
def part_2(data: List[List[str]]) -> int:

    accum = 0
    for line in data:

        l = line
        l.reverse()
        cnt = l[-1]

        while True:
        
            if all(x == 0 for x in l):
                break
        
            l = [b - a for a, b in zip(l[:-1], l[1:])]
            cnt += l[-1]
        
        accum += cnt        

    return accum


if __name__ == "__main__":
    data = read_input("../inputs/day_09.txt")
    part_1(data)
    part_2(data)
