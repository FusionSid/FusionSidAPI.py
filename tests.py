import asyncio
from fusionsid import RandomMeme, QRCode

async def e():
    meme = await QRCode().generate("https://google.com")
    # await meme
    await meme.save("e.png")

loop = asyncio.new_event_loop()
loop.run_until_complete(e())

