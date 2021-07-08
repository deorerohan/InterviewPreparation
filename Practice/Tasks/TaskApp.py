"""
Demonstrates a Rich "application" using the Layout and Live classes.
"""

from datetime import datetime

from rich import box
from rich.align import Align
from rich.console import Console, RenderGroup
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.syntax import Syntax
from rich.table import Table
from rich.text import Text

import itertools


class Task:
    newid = itertools.count()

    def __init__(self, task, reminderDate) -> None:

        self.taskID = next(Task.newid)
        self.taskText = task
        self.reminder = reminderDate
        self.tags = list()
        self.notes = ""

    def SetTag(self, tag):
        self.tags.append(tag)

    def AppendNote(self, note):
        self.notes += f"\n{note}"

    def CreatePanel(self):
        textToShow = f"{self.taskID}. {self.taskText} \n{self.reminder}"
        return Panel(textToShow)


class TaskApp:
    def make_layout(self) -> Layout:
        """Define the layout."""
        layout = Layout(name="root")

        layout.split(
            Layout(name="header", size=3),
            Layout(name="main", ratio=1),
        )
        layout["main"].split_row(
            Layout(name="side"),
            Layout(name="body", ratio=3, minimum_size=60),
        )
        layout["side"].split(Layout(name="box1"), Layout(name="box2"))
        return layout

    def make_sponsor_message(self) -> Panel:
        """Some example content."""
        table = Table(title="Star Wars Movies", expand=True, show_edge=False)

        table.add_column("Released", justify="right", style="cyan", no_wrap=True)
        table.add_column("Title", style="magenta")
        table.add_column("Box Office", style="green")

        table.add_row(
            "Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690"
        )
        table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
        table.add_row(
            "Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889"
        )

        myTask1 = Task("This is my first task", None)
        myTask2 = Task("This is my second task", None)
        table.add_row(
            myTask1.CreatePanel(), "Dec 16, 2016", myTask2.CreatePanel()
        )
        return Panel(table)

    def Header(self) -> Panel:
        """Display header with clock."""
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[b]Rich[/b] Layout application",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="white on blue")

    def make_syntax(self) -> Panel:
        code = """#Instructions

This will have some instructions like:
- make list
- some more list
- and more
        """
        syntax = Panel(code, border_style="green")
        return syntax

    job_progress = Progress(
        "{task.description}",
        SpinnerColumn(),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    )
    job_progress.add_task("[green]Cooking")
    job_progress.add_task("[magenta]Baking", total=200)
    job_progress.add_task("[cyan]Mixing", total=400)

    total = sum(task.total for task in job_progress.tasks)
    overall_progress = Progress()
    overall_task = overall_progress.add_task("All Jobs", total=int(total))

    progress_table = Table.grid(expand=True)
    progress_table.add_row(
        Panel(
            overall_progress,
            title="Overall Progress",
            border_style="green",
            padding=(2, 2),
        ),
        Panel(job_progress, title="[b]Jobs", border_style="red", padding=(1, 2)),
    )

    def MainFunc(self):
        console = Console()
        layout = self.make_layout()
        layout["header"].update(self.Header())
        layout["body"].update(self.make_sponsor_message())
        layout["box2"].update(self.make_syntax())
        layout["box1"].update(Panel(layout.tree, border_style="red"))

        while True:
            console.print(layout)
            usr_input = console.input()


if __name__ == "__main__":
    app = TaskApp()
    app.MainFunc()
