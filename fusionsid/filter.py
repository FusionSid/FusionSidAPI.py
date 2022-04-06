from typing import Literal
from datetime import datetime

from .http import HTTPClient
from .image import BaseImage


class FilteredImage(BaseImage):
    """The filtered image"""

    def __init__(self, image_bytes) -> None:
        super().__init__(image_bytes=image_bytes)
        self.created_at = datetime.now()


class Filter:
    @classmethod
    async def blur(cls, image_url: str, amount: int = 5):
        """
        Puts a blur filter on an image

        Parameters
        ----------
            :param: image_url (str): The url to the image you want to put the filter on

        Returns
        -------
            :class:`FilteredImage`
        """
        image = await HTTPClient().get_image(
            f"filter/blur?image_url={image_url}&amount={amount}"
        )
        return FilteredImage(image)

    @classmethod
    async def grey_scale(cls, image_url: str):
        """
        Puts a greyscale filter on an image

        Parameters
        ----------
            :param: image_url (str): The url to the image you want to put the filter on

        Returns
        -------
            :class:`FilteredImage`
        """
        image = await HTTPClient().get_image(f"filter/greyscale?image_url={image_url}")
        return FilteredImage(image)

    @classmethod
    async def color(
        cls,
        image_url: str,
        color: Literal[
            "red", "green", "blue", "purple", "pink", "yellow", "grey", "sepia"
        ],
    ):
        """
        Puts a color filter on an image

        Parameters
        ----------
            :param: image_url (str): The url to the image you want to put the filter on
            :param: color (Literal["red", "green", "blue", "purple", "pink", "yellow", "grey", "sepia"]): The color of the filter

        Returns
        -------
            :class:`FilteredImage`
        """
        image = await HTTPClient().get_image(
            f"filter/color?image_url={image_url}&color={color}"
        )
        return FilteredImage(image)
