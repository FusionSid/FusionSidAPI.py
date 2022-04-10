import asyncio

from rich.text import Text
from rich.panel import Panel
from rich.console import Console

import fusionsid

def main():
    console = Console()
    info_message = Text.from_markup(
        f"""\n
        [bold red underline]Library Info[/]

        [green yellow]Version: [blue]{fusionsid.__version__}[/]\t[green purple]Author: [blue]{fusionsid.__author__}[/]

        [bold red underline]Links[/]

        [green bold]API: [blue]{fusionsid.__url__}[/]

        [green bold]PyPi Link: [/][blue]https://pypi.org/project/fusionsidsapi/

        [green bold]API Wrapper Docs: [/][blue]https://fusionsid.github.io/FusionSidAPI.py/

        [green bold]Link to source code: [/][blue]https://github.com/FusionSid/FusionSidAPI.py
        """,
        justify="center",
    )

    thanks_panel = Panel(
        info_message,
        title="Thank you for using FusionSidAPI.py!",
        border_style="red",
    )
    console.print(thanks_panel)


if __name__ == "__main__":
    main()
