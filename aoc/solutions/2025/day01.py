"""Solution for Advent of Code 2025 Day 01."""


def part1(input_data: list[str]) -> int:
    moves = [x[0] for x in input_data]
    numbers = [int(x[1:]) for x in input_data]

    password = 0
    target = 50

    for move, num in zip(moves, numbers):
        if move == "R":
            target = (target + num) % 100
        if move == "L":
            target = (target - num) % 100
        if target == 0:
            password += 1

    return password


def part2(input_data: list[str]) -> int:
    moves = [x[0] for x in input_data]
    numbers = [int(x[1:]) for x in input_data]

    password = 0
    target = 50

    for move, num in zip(moves, numbers):
        delta_pwd = 0
        if move == "R":
            delta_pwd = (target + num) // 100
            target = (target + num) % 100
        if move == "L":
            if target == 0:
                delta_pwd = abs((target - num) // 100) - 1
            else:
                delta_pwd = abs((target - num) // 100)
            target = (target - num) % 100
            if target == 0:
                delta_pwd += 1

        password += delta_pwd

    return password
