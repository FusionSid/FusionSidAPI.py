import asyncio
from fusionsid import Fun

async def main():
    roast = await Fun.roast()
    print(roast)

    complement = await Fun.compliment()
    print(complement)
    
    fact = await Fun.fact()
    print(fact)

    search = await Fun.reddit_search("discord bots")
    print(search)

loop = asyncio.new_event_loop()
loop.run_until_complete(main())