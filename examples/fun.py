import asyncio
from fusionsid import Fun

async def main():
    roast = await Fun().roast()
    print(roast)

    complement = await Fun().compliment()
    print(complement)


loop = asyncio.new_event_loop()
loop.run_until_complete(main())