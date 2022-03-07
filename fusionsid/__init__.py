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
__version__ = "0.0.1"
__url__ = "https://fusionsidapi.herokuapp.com"
__github__ = "https://github.com/FusionSid/FusionSidAPI.py"
__api_github__ = "https://github.com/FusionSid/FusionSidsAPI"

async def stats(json=False):
    data = await HTTPClient().get_url_json(f"{__url__}/stats")

    if not json:
        print("\n".join([f"{k} = {v}" for k, v in data["stats"].items()]))
        return "\n"

    return data

async def endpoints(json=False):
    data = await HTTPClient().get_url_json(f"{__url__}/api") 
    endpoints = "\n".join([f"GET {i}" for i in data["endpoints"]])

    if not json:
        print(f"Base URL: {__url__}\n\nEndpoints:\n\n{endpoints}")
        return "\n"
        
    return data