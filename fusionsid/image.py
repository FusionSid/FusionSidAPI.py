from io import BytesIO
from datetime import datetime

import PIL
import aiohttp
import aiofiles
from PIL import Image as img

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

        async with aiofiles.open(path, "wb") as f:
            await f.write(self.image_bytes)

    async def show(self) -> None:

        """
        Shows an image
        """

        if self.image_bytes is None:
            raise ImageNotGenerated

        image = img.open(BytesIO(self.image_bytes))
        image.show()

        return None

    async def save_bytesio(self) -> BytesIO:

        """
        Saves the image to BytesIO

        Returns
        -------
            :class:`BytesIO`
        """

        if self.image_bytes is None:
            raise ImageNotGenerated

        image = BytesIO(self.image_bytes)

        return image

    async def pil(self) -> PIL.Image.Image:

        """
        Converts the image to a PIL.Image.Image object and returns it

        Returns
        -------
            :class:`PIL.Image.Image`
        """

        image = img.open(BytesIO(self.image_bytes))
        return image


class RandomMeme(BaseImage):
    """
    Random Meme
    -----------

    Example
    -------
        >>> meme = await Image.random_meme()
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
        return self.json["title"]

    @property
    def upvotes(self) -> str:
        """How many upvotes the meme has"""
        if self.image_bytes is None:
            raise ImageNotGenerated
        return self.json["upvotes"]

    @property
    def author(self) -> str:
        """Author of the post"""
        if self.image_bytes is None:
            raise ImageNotGenerated
        return self.json["author"]

    @property
    def url(self) -> str:
        """Url to the reddit post"""
        if self.image_bytes is None:
            raise ImageNotGenerated
        return self.json["url"]

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
        >>> qrcode = Image.qrcode("https://google.com")
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


class FontImage(BaseImage):
    """
    FontConvertedImage
    ------------------

    Attributes
    ----------
        created_at (datetime) : The time when the class was made
    """

    def __init__(self, image_bytes):
        self.created_at = datetime.now()
        super().__init__(image_bytes=image_bytes)


class Image:
    """
    Group of non meme generating image function
    -------------------------------------------

    Methods
    -------
        random_meme()
        qrcode(url : str)
        get_colors(filepath : str, show_hex : bool = True)

    """

    @classmethod
    async def random_meme(cls) -> RandomMeme:
        """
        Gets a random meme from the subreddit: r/memes

        Returns
        -------
            :class:`RandomMeme` : The meme
        """
        while True:
            image = await HTTPClient().get_json(url="meme?reddit_json_info=True")
            if "." in image["url"]:
                break
        image_url = image["url"]
        image_bytes = await HTTPClient().get_url_image(image_url)

        return RandomMeme(json=image, image_bytes=image_bytes)

    @classmethod
    async def qrcode(cls, url: str) -> QRCode:
        """
        Generates a qr code

        Returns
        -------
            :class:`QRCode` : The qrcode
        """
        qrcode = await HTTPClient().get_image(f"qrcode?link={url}")

        return QRCode(url, qrcode)

    @classmethod
    async def get_colors(cls, filepath: str, show_hex=True) -> dict:
        """
        Gets the most dominant color and color palette of an image

        Parameters
        ----------
            :param: filepath (str) : The path to the file
            :param: show_hex (bool) : By default the api will return hex values but if you want rgb set this to False

        Example
        -------
            >>> await Image.get_colors("snail.png", False)
        """
        try:
            with open(filepath, "rb") as f:
                image_in_bytes = f.read()

        except FileNotFoundError:
            return "File not found"

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"https://fusionsidapi.herokuapp.com/api/get_colors/?show_hex={show_hex}",
                data={"image": image_in_bytes},
            ) as resp:
                data = await resp.json()

        return data

    @classmethod
    async def font_convert(
        cls, text: str, font_name: str, color: str = "black"
    ) -> FontImage:
        """
        Converts text to a font you choose

        Parameters
        ----------
            :param text (str): The text you are converting
            :param font_name (str): The font you are converting to,
                Use the Image.font_list() function to get a list of them
            :param color (str, Optional): The color of the text, Defaults to black

        Returns
        -------
            :class:`FontImage`: The image of the font
        """
        list_of_fonts = await HTTPClient().get_json("fontconvert/list")
        list_of_fonts = list_of_fonts["Font_List"]

        if font_name not in list_of_fonts:
            url = "https://fusionsidapi.herokuapp.com/api/fontconvert/list"
            return print(
                f"Invalid font, go to {url} to get a list of them or use the font list function"
            )

        url = f"""fontconvert?text={text}&font={font_name}&color={color}"""
        image_bytes = await HTTPClient().get_image(url)

        return FontImage(image_bytes)

    @classmethod
    async def font_list(cls, print_all: bool = False) -> list:
        """
        Prints a list of all the fonts that the api supports converting to

        Parameters
        ----------
            :param print_all (bool, Optional): setting this to true will print all the fonts in console

        Returns
        -------
            :class:`list` : The list of fonts
        """
        list_of_fonts = await HTTPClient().get_json("fontconvert/list")
        list_of_fonts = list_of_fonts["Font_List"]

        if print_all:
            print("\n".join(list_of_fonts))
        return list_of_fonts


class Meme(BaseImage):
    """
    Meme
    ----

    Attributes
    ----------
        created_at (datetime) : The time when the class was made
    """

    def __init__(self, image_bytes):
        self.created_at = datetime.now()
        super().__init__(image_bytes=image_bytes)


class GenerateMeme:
    """
    Generate Meme
    -------------

    Methods
    -------
        abandon(text : str) : Returns a `Meme`

        armor(text : str) : Returns a `Meme`

        surprised(text : str) : Returns a `Meme`

        violence(text : str) : Returns a `Meme`

        bongocat(image_url : str) : Returns a `Meme`

        brazzers(image_url : str) : Returns a `Meme`

        gun(image_url : str) : Returns a `Meme`

        trash(image_url : str) : Returns a `Meme`

        aborted(image_url : str) : Returns a `Meme`

        affect(image_url : str) : Returns a `Meme`

        wanted(image_url : str) : Returns a `Meme`

    """

    @classmethod
    async def abandon(cls, text: str) -> Meme:
        """
        Generates the abandon meme

        Parameters
        ----------
            :param text : (str) : The text you want to use for the meme

        Returns
        -------
            :class:`Meme`

        """
        image_bytes = await HTTPClient().get_image(
            f"abandon?text={text.replace(' ', '+')}"
        )
        return Meme(image_bytes)

    @classmethod
    async def armor(cls, text: str) -> Meme:
        """
        Generates the armor meme

        Parameters
        ----------
            :param text : (str) : The text you want to use for the meme

        Returns
        -------
            :class:`Meme`

        """
        image_bytes = await HTTPClient().get_image(
            f"armor?text={text.replace(' ', '+')}"
        )
        return Meme(image_bytes)

    @classmethod
    async def surprised(cls, text: str) -> Meme:
        """
        Generates the surprised meme

        Parameters
        ----------
            :param text : (str) : The text you want to use for the meme

        Returns
        -------
            :class:`Meme`

        """
        image_bytes = await HTTPClient().get_image(
            f"surprised?text={text.replace(' ', '+')}"
        )
        return Meme(image_bytes)

    @classmethod
    async def violence(cls, text: str) -> Meme:
        """
        Generates the violence meme

        Parameters
        ----------
            :param text : (str) : The text you want to use for the meme

        Returns
        -------
            :class:`Meme`

        """
        image_bytes = await HTTPClient().get_image(
            f"violence?text={text.replace(' ', '+')}"
        )
        return Meme(image_bytes)

    @classmethod
    async def bongocat(cls, image_url: str) -> Meme:
        """
        Generates the bongocat meme

        Parameters
        ----------
            :param image_url : (str) : The image you want to use for the meme

        Returns
        -------
            :class:`Meme`

        """
        image_bytes = await HTTPClient().get_image(f"bongocat?image_url={image_url}")
        return Meme(image_bytes)

    @classmethod
    async def brazzers(cls, image_url: str) -> Meme:
        """
        Generates the brazzers meme

        Parameters
        ----------
            :param image_url : (str) : The image you want to use for the meme

        Returns
        -------
            :class:`Meme`

        """
        image_bytes = await HTTPClient().get_image(f"brazzers?image_url={image_url}")
        return Meme(image_bytes)

    @classmethod
    async def gun(cls, image_url: str) -> Meme:
        """
        Generates the gun meme

        Parameters
        ----------
            :param image_url : (str) : The image you want to use for the meme

        Returns
        -------
            :class:`Meme`

        """
        image_bytes = await HTTPClient().get_image(f"gun?image_url={image_url}")
        return Meme(image_bytes)

    @classmethod
    async def trash(cls, image_url: str) -> Meme:
        """
        Generates the trash meme

        Parameters
        ----------
            :param image_url : (str) : The image you want to use for the meme

        Returns
        -------
            :class:`Meme`

        """
        image_bytes = await HTTPClient().get_image(f"trash?image_url={image_url}")
        return Meme(image_bytes)

    @classmethod
    async def aborted(cls, image_url: str) -> Meme:
        """
        Generates the aborted meme

        Parameters
        ----------
            :param image_url : (str) : The image you want to use for the meme

        Returns
        -------
            :class:`Meme`

        """
        image_bytes = await HTTPClient().get_image(f"aborted?image_url={image_url}")
        return Meme(image_bytes)

    @classmethod
    async def affect(cls, image_url: str) -> Meme:
        """
        Generates the aborted meme

        Parameters
        ----------
            :param image_url : (str) : The image you want to use for the meme

        Returns
        -------
            :class:`Meme`

        """
        image_bytes = await HTTPClient().get_image(f"affect?image_url={image_url}")
        return Meme(image_bytes)

    @classmethod
    async def wanted(cls, image_url: str) -> Meme:
        """
        Generates the wanted meme

        Parameters
        ----------
            :param image_url : (str) : The image you want to use for the meme

        Returns
        -------
            :class:`Meme`

        """
        image_bytes = await HTTPClient().get_image(f"wanted?image_url={image_url}")
        return Meme(image_bytes)
