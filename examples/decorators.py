import asyncio
from fusionsid import Decorators

deco = Decorators

do_roast = deco.roast


@deco.compliment()  # will give you a complement before the function is run
@Decorators.fact()  # you can just put the class name and use that instead of setting it to a var
@do_roast()  # you can set it to a variable and use that
async def main():
    print("Wassup")


loop = asyncio.new_event_loop()
loop.run_until_complete(main())
