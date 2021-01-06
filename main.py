from rich.console   import Console
from rich.table     import Table
from rich.text      import Text
import typer

app = typer.Typer()


@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")

@app.command()
def table():
    table = Table(title=":christmas_tree: Welcome to Advent of Code 2020 :christmas_tree:", style="yellow")

    table.add_column("Day", justify="center", style="green")
    table.add_column("Title", style="cyan")
    table.add_column("Part 1", justify="center")
    table.add_column("Part 2", justify="center")

    table.add_row("01", "Report Repair", ":star:", ":star:")
    table.add_row("02", "Password Philosophy", ":star:", ":star:")
    table.add_row("03", "Toboggan Trajectory", ":star:", ":star:")
    table.add_row("04", "Passport Processing", ":star:", "")
    table.add_row("05", "Binary Boarding", ":star:", ":star:")
    table.add_row("06", "Custom Customs", ":star:", ":star:")


if __name__ == "__main__":
    app()
    c = Console()
    c.print(table)
    c.print("   You collected a total of 11/50 stars! :star:")

    # Hello!