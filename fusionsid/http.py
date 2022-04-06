import aiohttp
from typing import Dict


class HTTPClient:
    def __init__(self):
        self.BASE_URL = "https://fusionsidapi.herokuapp.com/api"

    async def get_image(self, url) -> bytes:
        """
        This function makes a get request to a url and returns the image

        Parameters
            :param url (str) : The url to make a request to

        Returns:
            :class:`bytes` : The image
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.BASE_URL}/{url}") as resp:
                resp = await resp.read()
        return resp

    async def get_url_image(self, url) -> bytes:
        """
        This function makes a get request to a url and returns the image

        Parameters
           :param url (str) : The url to make a request to

        Returns:
            :class:`bytes` : The image
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                resp = await resp.read()
        return resp

    async def get_json(self, url) -> Dict:
        """
        This function makes a GET request to a url and returns the json

        Parameters
            :param url (str) : The url to make a request to
            :param data (Dict, optional) : This is a dictionary of any extra params to send the request

        Returns:
            :class:`Dict` : The json response
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.BASE_URL}/{url}") as resp:
                try:
                    response = await resp.json()
                except Exception:
                    response = resp
        return response

    async def get_url_json(self, url) -> Dict:
        """
        This function makes a GET request to a url and returns the json

        Parameters
            :param url (str) : The url to make a request to
            :param data (Dict, optional) : This is a dictionary of any extra params to send the request

        Returns:
            :class:`Dict` : The json response
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                try:
                    response = await resp.json()
                except Exception:
                    response = resp
        return response
