from fusionsid.image import *
from fusionsid.misc import * 
from fusionsid.errors import *
from fusionsid.http import *
   
"""
FusionSidAPI
An asynchronous api wrapper for [FusionSidAPI](https://fusionsidapi.herokuapp.com).
"""

__title__ = "fusionsidapi"
__license__ = "MIT"
__author__ = "FusionSid"
__version__ = "0.0.5"
__url__ = "https://fusionsidapi.herokuapp.com"
__github__ = "https://github.com/FusionSid/FusionSidAPI.py"
__api_github__ = "https://github.com/FusionSid/FusionSidsAPI"

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