from .http import HTTPClient
from typing import *
import aiofiles
from .errors import *

class BaseImage:
    def __init__(self, image_bytes=None) -> None:
        self.image_bytes = image_bytes

    async def save(self, path: str) -> None:
        if self.image_bytes is None:
            raise ImageNotGenerated
        async with aiofiles.open(path, 'wb') as f:
            await f.write(self.image_bytes)


class RandomMeme(BaseImage):
    """
    ## Random Meme
    ----

    ### Example:
        >>> meme = Image().get_meme()
        >>> await meme.save('meme.png')

    ----

    ### Attrbutes:
        image_bytes : The image in bytes
        title (str) : Title of the post
        upvotes (str) : How many upvotes the meme has
        author (str) : Author of the meme
        url (str) : Url to the reddit post
        ext (str) : The file extension (eg: png)
        json (Dict) : The json response from the api
    """ 
    def __init__(self, json, image_bytes) -> None:
        self.json = json
        super().__init__(image_bytes=image_bytes)


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


class QRCode(BaseImage):
    """
    ## QR Code

    ----

    ### Example:
        >>> qrcode = Image().qrcode("https://google.com")
        >>> await meme.save('qrcode.png')
    
    ----

    ### Attrbutes:
        url (str) : The url that your making the meme for
        image_bytes : The image in bytes
    
    """
    def __init__(self, url, image_bytes):
        self.url = url
        super().__init__(image_bytes=image_bytes)


class Image():
    async def random_meme(self) -> RandomMeme:
        while True:
            image = await HTTPClient().get_json(url="meme?reddit_json_info=True")
            if '.' in image['url']:
                break
        image_url = image['url']
        image_bytes = await HTTPClient().get_url_image(image_url)

        return RandomMeme(json=image, image_bytes=image_bytes)


    async def qrcode(self, url) -> QRCode:
        qrcode = await HTTPClient().get_image(f"qrcode?link={url}")
        
        return QRCode(url, qrcode)


class Meme(BaseImage):
    """
    ## Meme
    """
    pass

class GenerateMeme():
    pass