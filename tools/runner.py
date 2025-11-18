#!/usr/bin/env python3
"""Entrypoint for Advent of Code."""

import argparse
import importlib
import time
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule

import rootutils
rootutils.setup_root(__file__, indicator=".project-root", pythonpath=True)

from aoc.utils import (
    resolve_paths,
    create_boilerplate,
    load_lines,
    infer_year_day,
)

console = Console()

def main() -> int:
    parser = argparse.ArgumentParser(description="Run Advent of Code.")
    parser.add_argument("-y", "--year", type=int)
    parser.add_argument("-d", "--day", type=int)
    parser.add_argument("-s", "--sample", action="store_true")
    args = parser.parse_args()

    year, day = infer_year_day(args.year, args.day)
    paths = resolve_paths(year, day)

    if not paths["problem"].exists():
        create_boilerplate(year, day, paths)
        console.print(
            Panel.fit(
                f"✨ Created boilerplate for [cyan]{year}[/] Day "
                f"[cyan]{day:02d}[/].\nRun the command again!",
                border_style="magenta",
            )
        )
        return 0

    module_name = f"aoc.solutions.{year}.day{day:02d}"
    try:
        module = importlib.import_module(module_name)
    except ImportError as exc:
        console.print(f"[red]❌ Failed to import {module_name}: {exc}")
        return 1

    part1 = getattr(module, "part1", None)
    part2 = getattr(module, "part2", None)
    if not callable(part1) or not callable(part2):
        console.print("[red]❌ Module must define part1() and part2().[/]")
        return 1

    input_path = paths["sample"] if args.sample else paths["input"]
    input_data = load_lines(input_path)

    if args.sample and not input_data:
        console.print(
            Panel.fit(
                f"[yellow]⚠️  No sample input found for {year} Day {day:02d}.[/]\n"
                "Exiting.",
                border_style="yellow",
            )
        )
        return 1

    console.print()
    console.print(
        Rule(
            f"🎄 Advent of Code {year} — Day {day:02d} "
            f"({'Sample' if args.sample else 'Real'})",
            style="green",
        )
    )

    start = time.perf_counter()
    p1 = part1(input_data)
    p2 = part2(input_data)
    end = time.perf_counter()

    console.print(Panel(f"🧩 Part 1:\n[bold green]{p1}[/]", border_style="cyan"))
    console.print(Panel(f"🧩 Part 2:\n[bold green]{p2}[/]", border_style="cyan"))

    console.print(
        f"[bold blue]⏰ Execution Time:[/] {(end - start) * 1000:.2f} ms"
    )
    console.print(Rule(style="dim"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
