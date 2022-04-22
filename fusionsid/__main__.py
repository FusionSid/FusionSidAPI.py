import inspect
import asyncio

import argparse
from rich.text import Text
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt, Confirm

import fusionsid


async def get_api_stats():
    console = Console()
    stats = await fusionsid.stats(json=True)

    sys_stats = "\n".join(
        [
            f"[blue]{key}:[/] [red]{value}[/]"
            for key, value in stats["system_stats"].items()
        ]
    )

    table = Table(
        title="[bold blue underline]Endpoint Stats[/]", title_justify="center"
    )
    table.add_column("Endpoint", justify="center", style="blue", no_wrap=True)
    table.add_column("Request Count", justify="center", style="red", no_wrap=True)

    for endpoint_name, endpoint_count in stats["stats"].items():
        table.add_row(endpoint_name, str(endpoint_count))

    other_stats = Text.from_markup(
        f"""
[bold blue]Uptime:[/][red]{stats['uptime']}[/]
\n[bold blue underline]System Stats:[/]\n{sys_stats}
    """
    )

    message = Table.grid(padding=2)
    message.add_column(no_wrap=True, justify="center")
    message.add_row(table)
    message.add_row(other_stats)

    panel = Panel(
        message,
        title="FusionSidsAPI Stats",
        title_align="center",
        border_style="red",
        subtitle="Thank you for using this api",
    )
    console.print(panel, justify="center")


def main() -> int:
    console = Console()
    parser = argparse.ArgumentParser()

    parser.add_argument("--api", action="store_true")
    parser.add_argument("--docs", action="store_true")
    parser.add_argument("--pypi", action="store_true")
    parser.add_argument("--github", action="store_true")

    parser.add_argument("--stats", action="store_true")

    # parser.add_argument("--image", action="store_true")
    # parser.add_argument("--meme", action="store_true")
    parser.add_argument("--fun", action="store_true")
    parser.add_argument("--text", action="store_true")
    # parser.add_argument("--filter", action="store_true")

    args = parser.parse_args()

    if len([value for key, value in args.__dict__.items() if value is False]) == len(
        list(args.__dict__.keys())
    ):
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
        console.print(thanks_panel, justify="center")
        return 0

    if args.api:
        console.print("\n[blue]https://api.fusionsid.xyz/docs[/]\n")
    if args.pypi:
        console.print("\n[blue]https://pypi.org/project/fusionsidsapi/[/]\n")
    if args.github:
        console.print("\n[blue]https://github.com/FusionSid/FusionSidAPI.py[/]\n")
    if args.docs:
        console.print("\n[blue]https://fusionsid.github.io/FusionSidAPI.py/[/]\n")


    if args.stats:
        loop = asyncio.new_event_loop()
        loop.run_until_complete(get_api_stats())

         
    if args.fun:
        functions = {
            key: value
            for key, value in fusionsid.Fun.__dict__.items()
            if key.startswith("__") is False
        }
        
        function_names_list = "\n".join(
            [f"{index}: {item}" for index, item in enumerate(functions)]
        )
        console.print(function_names_list)

        number = Prompt.ask("[blue]Enter the number for the function you want to run")
        function_name = list(functions.keys())[int(number)]
        function = functions[function_name].__func__

        function_params = (
            str(inspect.signature(function))
            .split("(")[1]
            .split(")")[0]
            .replace(" ", "")
            .split(",")
        )[1:]

        if len(function_params) == 0:
            run = Confirm.ask("Run function?")
            if run:
                output = asyncio.run(function(fusionsid.Fun))
                console.print(output)
                return 0

        else:
            params_given = []
            for param in function_params:
                    if "=" in param: continue
                    else:
                        name, type_ = param.split(':')[0], param.split(':')[1]
                        console.print(f"[blue]Enter the value for the [green]{name}[/] [blue]parameter with type:[/] [green]{type_}[/]")
                        param_given = Prompt.ask("Enter value")
                        if "int" in type_.lower():
                            param_given = int(param_given)
                        params_given.append(param_given)

        output = asyncio.run(function(fusionsid.Fun, *params_given))
        print(output)
        return 0

    if args.text:
        functions = {
            key: value
            for key, value in fusionsid.Text.__dict__.items()
            if key.startswith("__") is False
        }
        
        function_names_list = "\n".join(
            [f"{index}: {item}" for index, item in enumerate(functions)]
        )
        console.print(function_names_list)

        number = Prompt.ask("[blue]Enter the number for the function you want to run")
        function_name = list(functions.keys())[int(number)]
        function = functions[function_name].__func__

        function_params = (
            str(inspect.signature(function))
            .split("(")[1]
            .split(")")[0]
            .replace(" ", "")
            .split(",")
        )[1:]

        if len(function_params) == 0:
            run = Confirm.ask("Run function?")
            if run:
                output = asyncio.run(function(fusionsid.Text))
                console.print(output)
                return 0

        else:
            params_given = []
            for param in function_params:
                    if "=" in param: continue
                    else:
                        name, type_ = param.split(':')[0], param.split(':')[1]
                        console.print(f"[blue]Enter the value for the [green]{name}[/] [blue]parameter with type:[/] [green]{type_}[/]")
                        param_given = Prompt.ask("Enter value")
                        if "int" in type_.lower():
                            param_given = int(param_given)
                        params_given.append(param_given)

        output = asyncio.run(function(fusionsid.Text, *params_given))
        print(output)
        return 0
        

    return 0


if __name__ == "__main__":
    exit(main())
