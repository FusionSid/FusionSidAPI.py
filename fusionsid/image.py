from .http import HTTPClient
from typing import *
import aiofiles
from .errors import *

class Image:
    def __init__(self) -> None:
        self.image_bytes = None

    async def save(self, path: str) -> None:
        if self.image_bytes is None:
            raise ImageNotGenerated
        async with aiofiles.open(path, 'wb') as f:
            await f.write(self.image_bytes)


class RandomMeme(Image):
    """
    ## Random Meme

    Must be generated first using `get_meme()`

    ----

    ### Example:
        >>> meme = RandomMeme()
        >>> await meme.get_meme()
        >>> await meme.save('meme.png')

    ----

    ### Attrbutes:
        Must be generated first using `get_meme()`

        image_bytes : The image in bytes
        title (str) : Title of the post
        upvotes (str) : How many upvotes the meme has
        author (str) : Author of the meme
        url (str) : Url to the reddit post
        ext (str) : The file extension (eg: png)
        json (Dict) : The json response from the api
    """
    
    async def get_meme(self) -> None:
        while True:
            image = await HTTPClient().get_json(url="meme?reddit_json_info=True")
            if '.' in image['url']:
                break

        
        self.json = image

        image_url = image['url']

        image_bytes = await HTTPClient().get_url_image(image_url)

        self.image_bytes = image_bytes
        

    @property
    def title(self) -> str:
        if self.image_bytes is None:
            raise ImageNotGenerated
        return self.json['title']


    @property
    def upvotes(self) -> str:
        if self.image_bytes is None:
            raise ImageNotGenerated
        return self.json['upvotes']

    
    @property
    def author(self) -> str:
        if self.image_bytes is None:
            raise ImageNotGenerated
        return self.json['author']

    
    @property
    def url(self) -> str:
        if self.image_bytes is None:
            raise ImageNotGenerated
        return self.json['url']


    @property
    def ext(self) -> str:
        if self.image_bytes is None:
            raise ImageNotGenerated
        return self.json["url"].split(".")[-1]


class QRCode(Image):
    """
    ## QR Code

    Must be generated first using `QRCode.generate()`

    ----

    ### Example:
        >>> qrcode = QRCode()
        >>> await qrcode.generate("https://google.com")
        >>> await meme.save('qrcode.png')
    
    ----

    ### Attrbutes:
        Must be generated first using `QRCode.generate()`

        url (str) : The url that your making the meme for
        image_bytes : The image in bytes
    
    """
    async def generate(self, url) -> None:
        qrcode = await HTTPClient().get_image(f"qrcode?link={url}")
        self.image_bytes = qrcode
        self.url = url