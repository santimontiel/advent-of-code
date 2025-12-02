#!/usr/bin/env python3
"""Auto-run AoC solution on save with Rich console output."""

import argparse
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
import importlib

import rootutils
rootutils.setup_root(__file__, indicator=".project-root", pythonpath=True)

from aoc.utils import (
    infer_year_day,
    resolve_paths,
    create_boilerplate,
    load_lines,
)

console = Console()


class AoCAutoRunner(FileSystemEventHandler):
    """Automatically run AoC solution on file save."""

    def __init__(self, year: int, day: int, sample: bool):
        self.year = year
        self.day = day
        self.sample = sample
        self.paths = resolve_paths(year, day)
        self.last_modified = 0.0

        if not self.paths["problem"].exists():
            create_boilerplate(year, day, self.paths)
            console.print(f"✨ Created boilerplate for {year} Day {day:02d}.")
            console.print("Save the file again to run the solution.")

    def on_modified(self, event):
        if Path(event.src_path).resolve() == self.paths["problem"].resolve():
            mtime = self.paths["problem"].stat().st_mtime
            if mtime != self.last_modified:
                self.last_modified = mtime
                self.run_solution()

    def run_solution(self):
        console.clear()
        console.rule(f"🚀 Running AoC {self.year} Day {self.day:02d}")

        module_name = f"aoc.solutions.{self.year}.day{self.day:02d}"
        try:
            module = importlib.reload(importlib.import_module(module_name))
        except ImportError as exc:
            console.print(f"❌ [red]Failed to import module:[/] {exc}")
            return

        part1 = getattr(module, "part1", None)
        part2 = getattr(module, "part2", None)
        if not callable(part1) or not callable(part2):
            console.print("[red]❌ Module must define part1() and part2().[/]")
            return

        input_path = self.paths["sample"] if self.sample else self.paths["input"]
        input_data = load_lines(input_path)

        if args.sample and not input_data:
            console.print(
                Panel.fit(
                    f"[yellow]⚠️  No sample input found for {self.year} Day {self.day:02d}.[/]\n"
                    "Running with real input instead.",
                    border_style="yellow",
                )
            )
            input_path = self.paths["input"]
            input_data = load_lines(input_path)

        start = time.perf_counter()
        try:
            p1 = part1(input_data)
            p2 = part2(input_data)
        except Exception as e:
            console.print(f"❌ [red]Error during execution:[/] {e}")
            return
        elapsed = (time.perf_counter() - start) * 1000

        console.print(Panel(f"🧩 Part 1:\n[bold green]{p1}[/]", border_style="cyan"))
        console.print(Panel(f"🧩 Part 2:\n[bold green]{p2}[/]", border_style="cyan"))
        console.print(f"⏱️ [cyan]Execution Time:[/] {elapsed:.2f} ms")
        console.rule("[dim]Waiting for changes...")


def watch(year: int, day: int, sample: bool):
    runner = AoCAutoRunner(year, day, sample)
    observer = Observer()
    observer.schedule(runner, path=str(runner.paths["problem"].parent), recursive=False)
    observer.start()

    console.print(f"👀 [bold magenta]Watching AoC {year} Day {day:02d} solution file[/]\n")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auto-run AoC solution on save.")
    parser.add_argument("-y", "--year", type=int)
    parser.add_argument("-d", "--day", type=int)
    parser.add_argument("-s", "--sample", action="store_true")
    args = parser.parse_args()

    year, day = infer_year_day(args.year, args.day)

    watch(year, day, args.sample)