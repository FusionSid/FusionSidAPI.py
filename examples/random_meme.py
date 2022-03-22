import asyncio
from fusionsid import Image

async def main():
    meme = await Image.random_meme()
    await meme.save("random_meme.png")

    print(f"{meme.title} | {meme.author}")

loop = asyncio.new_event_loop()
loop.run_until_complete(main())