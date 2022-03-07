import asyncio
from fusionsid import Fun

async def main():
    # Prints a truth
    print(await Fun().truth())
   
    # Prints a dare
    print(await Fun().dare())

    # Returns a dict with both truth and dare and the computers choice
    print(await Fun().truth_or_dare())


loop = asyncio.new_event_loop()
loop.run_until_complete(main())