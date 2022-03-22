import asyncio
from fusionsid import Text

async def main():
    text_convert = Text()

    print(await text_convert.text_to_binary("Hello"))
    
    print(await text_convert.hash("lol"))

    print(await text_convert.binary_to_text("1101100 1101111 1101100"))

    print(await text_convert.expand("6c 6f 6c"))

loop = asyncio.new_event_loop()
loop.run_until_complete(main())