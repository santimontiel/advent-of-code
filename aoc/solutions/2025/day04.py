"""Solution for Advent of Code 2025 Day 04."""
from copy import deepcopy

def parse_input(input_data: list[str]) -> dict[tuple[int, int], bool]:

    # Store positions for all rolls.
    rolls = {}
    for y, line in enumerate(input_data):
        for x, char in enumerate(line):
            if char == "@":
                rolls[(x, y)] = True

    return rolls


def part1(input_data: list[str]) -> int:

    rolls = parse_input(input_data)
    
    # Evaluate the grid.
    with_access = 0
    for y, line in enumerate(input_data):
        for x, char in enumerate(line):
            if rolls.get((x, y), False):
                with_access += sum([
                    rolls.get((x - 1, y - 1), False),
                    rolls.get((x - 1, y), False),
                    rolls.get((x - 1, y + 1), False),
                    rolls.get((x, y - 1), False),
                    rolls.get((x, y + 1), False),
                    rolls.get((x + 1, y - 1), False),
                    rolls.get((x + 1, y), False),
                    rolls.get((x + 1, y + 1), False),
                ]) < 4
    
    return with_access



def part2(input_data: list[str]) -> int:
    
    rolls = parse_input(input_data)
    
    # Evaluate the grid iteratively.
    global_with_access = 0
    running = True
    while running:

        # Step through the grid.
        local_with_access = 0
        to_delete = list()
        for y, line in enumerate(input_data):
            for x, char in enumerate(line):
                if rolls.get((x, y), False):
                    neighbours = [
                        rolls.get((x - 1, y - 1), False),
                        rolls.get((x - 1, y), False),
                        rolls.get((x - 1, y + 1), False),
                        rolls.get((x, y - 1), False),
                        rolls.get((x, y + 1), False),
                        rolls.get((x + 1, y - 1), False),
                        rolls.get((x + 1, y), False),
                        rolls.get((x + 1, y + 1), False),
                    ]
                    if sum(neighbours) < 4:
                        local_with_access += 1
                        to_delete.append((x, y))
        
        # Update accesed rolls for this step.
        global_with_access += local_with_access
        for p in to_delete:
            rolls.pop(p)

        # Should we continue looping?
        if local_with_access == 0:
            running = False

    return global_with_access
