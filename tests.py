import asyncio
import fusionsid
from fusionsid import Image, Fun

async def test():
    print(await fusionsid.stats())
   


loop = asyncio.new_event_loop()
loop.run_until_complete(test())

