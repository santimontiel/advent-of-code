from typing import Dict, List
from utils import summary


def read_input(file_name: str) -> List[str]:
    with open(file_name, "r") as fin:
        workflows, ratings = fin.read().split("\n\n")
    w, r = workflows.splitlines(), ratings.splitlines()

    # Create a dict of workflow rules.
    workflows = {}
    for line in w:
        name, rules = line[:-1].split("{")
        rules = rules.split(",")
        workflows[name] = rules

    # Create a list of ratings.
    ratings = []
    for line in r:
        l = line[1:-1].split(",")
        l = list(map(lambda x: int(x[2:]), l))
        ratings.append(l)

    return workflows, ratings


def solve(rating: List[int], workflows: Dict[str, List[str]], start: str = "in") -> str:
    
    x, m, a, s = rating

    w = workflows[start]
    for rule in w:

        if ":" in rule:
            cmd, send = rule.split(":")
            pred = eval(cmd)
            if pred:
                if send in ["A", "R"]:
                    return send
                return solve(rating, workflows, send)
        else:
            cmd = rule
            if cmd in ["A", "R"]:
                return cmd
            return solve(rating, workflows, cmd)


@summary
def part_1(workflows: List[str], ratings: List[int]) -> int:
    
    total = 0
    for r in ratings:
        answer = solve(r, workflows)
        total += sum(r) if answer == "A" else 0

    return total


def main() -> None:
    w, r = read_input("../inputs/day_19.txt")
    part_1(w, r)


if __name__ == "__main__":
    main()