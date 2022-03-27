import asyncio
from fusionsid import GenerateMeme


async def main():
    # Example 1
    meme = await GenerateMeme.trash(
        "https://variety.com/wp-content/uploads/2021/07/Rick-Astley-Never-Gonna-Give-You-Up.png"
    )
    await meme.save("meme1.png")

    # Example 2
    meme2 = await GenerateMeme.abandon("I like light theme")
    await meme2.save("meme2.png")


loop = asyncio.new_event_loop()
loop.run_until_complete(main())
