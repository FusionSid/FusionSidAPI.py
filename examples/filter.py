import asyncio
from fusionsid import Filter


async def main():
    # Example 1
    image1 = await Filter.blur(
        "https://cdn.discordapp.com/avatars/624076054969188363/aa95053525ab5f423202617ac1c214f5.png?size=1024"
    )
    await image1.save("image1.png")

    # Example 2
    image2 = await Filter.color(
        "https://cdn.discordapp.com/avatars/624076054969188363/aa95053525ab5f423202617ac1c214f5.png?size=1024",
        "sepia",
    )
    await image2.save("image2.png")
    


loop = asyncio.new_event_loop()
loop.run_until_complete(main())
