"""Solution for Advent of Code 2015 Day 03."""


def part1(input_data: list[str]) -> int:
    moves = input_data[0]
    current_position = 0 + 0j
    positions = [current_position]

    for move in moves:
        if move == "^":
            current_position += 1
        elif move == "v":
            current_position -= 1
        elif move == ">":
            current_position += 1j
        elif move == "<":
            current_position -= 1j
        positions.append(current_position)
    
    return len(set(positions))


def part2(input_data: list[str]) -> int:
    moves = input_data[0]
    current_position = 0 + 0j
    robot_current_position = 0 + 0j
    positions = [current_position, robot_current_position]

    for i, move in enumerate(moves):
        if move == "^":
            delta = 1
        elif move == "v":
            delta = -1
        elif move == ">":
            delta = 1j
        elif move == "<":
            delta = -1j

        if i % 2 == 0:
            current_position += delta
            positions.append(current_position)
        else:
            robot_current_position += delta
            positions.append(robot_current_position)
    
    return len(set(positions))
