from typing import Dict

from fusionsid.decorators import Decorators
from fusionsid.errors import Error, ImageNotGenerated
from fusionsid.fun import Fun
from fusionsid.http import HTTPClient
from fusionsid.image import BaseImage, RandomMeme, QRCode, Image, Meme, GenerateMeme, FontImage
from fusionsid.text import Text

   
"""
FusionSidAPI
An asynchronous api wrapper for [FusionSidAPI](https://fusionsidapi.herokuapp.com).
"""

__title__ = "fusionsidapi"
__license__ = "MIT"
__author__ = "FusionSid"
__version__ = "0.0.11"
__url__ = "https://fusionsidapi.herokuapp.com"
__github__ = "https://github.com/FusionSid/FusionSidAPI.py"
__api_github__ = "https://github.com/FusionSid/FusionSidsAPI"
__docs__ = "https://fusionsid.github.io/FusionSidAPI.py/"


async def stats(json=False) -> Dict:
    """
    Stats about the api

    Returns:
        Dict
    """
    data = await HTTPClient().get_url_json(f"{__url__}/stats")

    if json == False:
        api_stats = "\n".join([f"{k} = {v}" for k, v in data["stats"].items()])
        api_system_stats = "\n".join([f"{k} = {v}" for k, v in data["system_stats"].items()])
        return f"{api_stats}\n\n{api_system_stats}"

    return data


async def endpoints(json=False) -> Dict:
    """
    List of api endpoints

    Returns:
        Dict
    """
    data = await HTTPClient().get_url_json(f"{__url__}/api") 
    endpoints = "\n".join([f"GET {i}" for i in data["endpoints"]])

    if not json:
        return f"Base URL: {__url__}\n\nEndpoints:\n\n{endpoints}"
        
    return data