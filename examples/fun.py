import asyncio
from fusionsid import Fun

async def main():
    roast = await Fun().roast()
    print(roast)

    complement = await Fun().compliment()
    print(complement)
    
    fact = await Fun().fact()
    print(fact)

    # There is more endpoints (eg 8ball) these are just some examples

loop = asyncio.new_event_loop()
loop.run_until_complete(main())