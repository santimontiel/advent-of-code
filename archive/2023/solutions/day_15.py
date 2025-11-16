from typing import List
from utils import summary
from dataclasses import dataclass

def read_input(file_name: str) -> List[str]:
    with open(file_name, "r") as fin:
        return fin.read().split(",")
    

@summary
def part_1(data: List[str]) -> int: 

    values = []
    for string in data:
        curr_value = 0
        for char in string:
            curr_value = (ord(char) + curr_value) * 17 % 256
        values.append(curr_value)

    return sum(values)

@dataclass
class Lens:
    label: str
    focal_length: int

@summary
def part_2(data: List[str]) -> int:

    def get_box(string: str) -> int:
        curr_value = 0
        for char in string:
            curr_value = (ord(char) + curr_value) * 17 % 256
        return curr_value

    boxes = {i: [] for i in range(256)}
    for string in data:

        # Parse the string.
        if string[-1] == "-":
            label, op, arg = string[:-1], "-", None
            box = get_box(label)
        else:
            label, op, arg = string[:-2], string[-2], int(string[-1])
            box = get_box(label)

        # Perform the operation.
        if op == "=":
            for lens in boxes[box]:
                if lens.label == label:
                    lens.focal_length = arg
                    break
            else:
                boxes[box].append(Lens(label, arg))
        if op == "-":
            for lens in boxes[box]:
                if lens.label == label:
                    boxes[box].remove(lens)
                    break


    # Compute focusing power.
    power = 0
    for k, v in boxes.items():
        for i, lens in enumerate(v):
            power += (k + 1) * (i + 1) * lens.focal_length

    return power



def main() -> None:
    data = read_input("../inputs/day_15.txt")
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
   