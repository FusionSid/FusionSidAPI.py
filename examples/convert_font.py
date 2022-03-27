import asyncio
import random
from fusionsid import Image


async def main():
    # Get a list of fonts supported
    font_list = await Image.font_list(print_all=False)

    # Chooses a random font
    font = random.choice(font_list)

    # Converts text "Hello World" to that font
    image = await Image.font_convert("Hello World", font)

    # Shows the image
    await image.show()


loop = asyncio.new_event_loop()
loop.run_until_complete(main())
