from datetime import datetime

import aiofiles

from .http import HTTPClient
from .errors import ImageNotGenerated

class BaseImage:
    """
    Base class for all images
    -------------------------

    Methods
    -------
        save(path : str) : Saves the file to a path
    """
    def __init__(self, image_bytes=None) -> None:
        self.image_bytes = image_bytes

    async def save(self, path: str) -> None:
        """
        Saves an image
        """
        if self.image_bytes is None:
            raise ImageNotGenerated
        async with aiofiles.open(path, 'wb') as f:
            await f.write(self.image_bytes)


class RandomMeme(BaseImage):
    """
    Random Meme
    -----------

    Example
    -------
        >>> meme = await Image().random_meme()
        >>> await meme.save('meme.png')

    Attrbutes
    ---------
        image_bytes (bytes) : The image in bytes
        title (str) : Title of the post
        upvotes (str) : How many upvotes the meme has
        author (str) : Author of the meme
        url (str) : Url to the reddit post
        ext (str) : The file extension (eg: png)
        json (Dict) : The json response from the api
        created_at (datetime.datetime) : The time when the class was made
    """ 
    
    def __init__(self, json, image_bytes) -> None:
        self.json = json
        super().__init__(image_bytes=image_bytes)
        self.created_at = datetime.now()


    @property
    def title(self) -> str:
        """The title of the meme"""
        if self.image_bytes is None:
            raise ImageNotGenerated
        return self.json['title']


    @property
    def upvotes(self) -> str:
        """How many upvotes the meme has"""
        if self.image_bytes is None:
            raise ImageNotGenerated
        return self.json['upvotes']

    
    @property
    def author(self) -> str:
        """Author of the post"""
        if self.image_bytes is None:
            raise ImageNotGenerated
        return self.json['author']

    
    @property
    def url(self) -> str:
        """Url to the reddit post"""
        if self.image_bytes is None:
            raise ImageNotGenerated
        return self.json['url']


    @property
    def ext(self) -> str:
        """The file extension"""
        if self.image_bytes is None:
            raise ImageNotGenerated
        return self.json["url"].split(".")[-1]


class QRCode(BaseImage):
    """
    QR Code
    -------

    Example
    -------
        >>> qrcode = Image().qrcode("https://google.com")
        >>> await meme.save('qrcode.png')

    Attrbutes
    ---------
        url (str) : The url that your making the meme for
        image_bytes (bytes) : The image in bytes
        created_at (datetime) : The time when the class was made
    
    """
    def __init__(self, url, image_bytes):
        self.url = url
        self.created_at = datetime.now()
        super().__init__(image_bytes=image_bytes)


class Image():
    """
    Group of non meme generating image function
    -------------------------------------------

    Methods
    -------
        random_meme()
        qrcode(url : str)
    
    """

    @classmethod
    async def random_meme(self) -> RandomMeme:
        """
        Gets a random meme from the subreddit: r/memes
        
        Returns:
            RandomMeme : The meme
        """
        while True:
            image = await HTTPClient().get_json(url="meme?reddit_json_info=True")
            if '.' in image['url']:
                break
        image_url = image['url']
        image_bytes = await HTTPClient().get_url_image(image_url)

        return RandomMeme(json=image, image_bytes=image_bytes)


    @classmethod
    async def qrcode(self, url : str) -> QRCode:
        """
        Generates a qr code

        Returns:
            QRCode : The qrcode
        """
        qrcode = await HTTPClient().get_image(f"qrcode?link={url}")
        
        return QRCode(url, qrcode)


class Meme(BaseImage):
    """
    Meme
    ----

    Attributes
    ----------
        created_at (datetime) : The time when the class was made
    """
    def __init__(self):
        self.created_at = datetime.now()

class GenerateMeme():
    """
    Generate Meme
    -------------

    Methods
    -------
        abandon(text : str) : Returns a `Meme`
        aborted(image_url : str) : Returns a `Meme`
        affect(image_url : str) : Returns a `Meme`
        armor(text : str) : Returns a `Meme`
        bongocat(image_url : str) : Returns a `Meme`
        brazzers(image_url : str) : Returns a `Meme`
        gun(image_url : str) : Returns a `Meme`
        surprised(text : str) : Returns a `Meme`
        trash(image_url : str) : Returns a `Meme`
        violence(text : str) : Returns a `Meme`
        wanted(image_url : str) : Returns a `Meme`
    """

    @classmethod
    async def abandon(self, text : str) -> Meme:
        """
        Generates the abandon meme

        Parameters
            :param text : (str) : The text you want to use for the meme

        """
        image_bytes = await HTTPClient().get_image(f"abandon?text={text.replace(' ', '+')}")
        return Meme(image_bytes)
    

    @classmethod
    async def aborted(self, image_url : str) -> Meme:
        """
        Generates the aborted meme

        Parameters
            :param image_url : (str) : The image you want to use for the meme

        """
        image_bytes = await HTTPClient().get_image(f"aborted?image_url={image_url}")
        return Meme(image_bytes)
    

    @classmethod
    async def affect(self, image_url : str) -> Meme:
        """
        Generates the aborted meme

        Parameters
            :param image_url : (str) : The image you want to use for the meme

        """
        image_bytes = await HTTPClient().get_image(f"affect?image_url={image_url}")
        return Meme(image_bytes)
    

    @classmethod
    async def armor(self, text : str) -> Meme:
        """
        Generates the armor meme

        Parameters
            :param text : (str) : The text you want to use for the meme

        """
        image_bytes = await HTTPClient().get_image(f"armor?text={text.replace(' ', '+')}")
        return Meme(image_bytes)
    

    @classmethod
    async def bongocat(self, image_url : str) -> Meme:
        """
        Generates the bongocat meme

        Parameters
            :param image_url : (str) : The image you want to use for the meme

        """
        image_bytes = await HTTPClient().get_image(f"bongocat?image_url={image_url}")
        return Meme(image_bytes)
    

    @classmethod
    async def brazzers(self, image_url : str) -> Meme:
        """
        Generates the brazzers meme

        Parameters
            :param image_url : (str) : The image you want to use for the meme

        """
        image_bytes = await HTTPClient().get_image(f"brazzers?image_url={image_url}")
        return Meme(image_bytes)
    

    @classmethod
    async def gun(self, image_url : str) -> Meme:
        """
        Generates the gun meme

        Parameters
            :param image_url : (str) : The image you want to use for the meme

        """
        image_bytes = await HTTPClient().get_image(f"gun?image_url={image_url}")
        return Meme(image_bytes)
    

    @classmethod
    async def surprised(self, text : str) -> Meme:
        """
        Generates the surprised meme

        Parameters
            :param text : (str) : The text you want to use for the meme

        """
        image_bytes = await HTTPClient().get_image(f"surprised?text={text.replace(' ', '+')}")
        return Meme(image_bytes)
    

    @classmethod
    async def trash(self, image_url : str) -> Meme:
        """
        Generates the trash meme

        Parameters
            :param image_url : (str) : The image you want to use for the meme

        """
        image_bytes = await HTTPClient().get_image(f"trash?image_url={image_url}")
        return Meme(image_bytes)
    

    @classmethod
    async def violence(self, text : str) -> Meme:
        """
        Generates the violence meme

        Parameters
            :param text : (str) : The text you want to use for the meme

        """
        image_bytes = await HTTPClient().get_image(f"violence?text={text.replace(' ', '+')}")
        return Meme(image_bytes)
    

    @classmethod
    async def wanted(self, image_url : str) -> Meme:
        """
        Generates the wanted meme

        Parameters
            :param image_url : (str) : The image you want to use for the meme

        """
        image_bytes = await HTTPClient().get_image(f"wanted?image_url={image_url}")
        return Meme(image_bytes)