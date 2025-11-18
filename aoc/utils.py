"""Shared utilities for AoC runner scripts."""
from pathlib import Path
from datetime import datetime


def resolve_paths(year: int, day: int) -> dict[str, Path]:
    return {
        "problem": Path(f"aoc/solutions/{year}/day{day:02d}.py"),
        "input": Path(f"data/{year}/day{day:02d}_input.txt"),
        "sample": Path(f"data/{year}/day{day:02d}_sample.txt"),
    }


def create_boilerplate(year: int, day: int, paths: dict[str, Path]) -> None:
    for p in paths.values():
        p.parent.mkdir(parents=True, exist_ok=True)

    boilerplate = (
        f'"""Solution for Advent of Code {year} Day {day:02d}."""\n\n'
        "def part1(input_data: list[str]) -> int:\n"
        "    pass\n\n"
        "def part2(input_data: list[str]) -> int:\n"
        "    pass\n"
    )
    paths["problem"].write_text(boilerplate, encoding="utf-8")
    paths["input"].touch()
    paths["sample"].touch()


def load_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def infer_year_day(year: int | None, day: int | None) -> tuple[int, int]:
    now = datetime.now()

    if year is None and day is None:
        if now.month != 12:
            raise ValueError("Not December — specify --year and --day.")
        return now.year, now.day

    return year or now.year, day or now.day
