from fusionsid.image import *
from fusionsid.misc import * 
from fusionsid.errors import *
from fusionsid.http import *

   
"""
FusionSidAPI
An asynchronous (badly coded) wrapper for FusionSidAPI.
"""

__title__ = "fusionsidapi"
__license__ = "MIT"
__author__ = "FusionSid"
__version__ = "0.0.1"
__url__ = "https://fusionsidapi.herokuapp.com"

async def stats(json=False):
    data = await HTTPClient().get_url_json(f"{__url__}/stats")

    if not json:
        print("\n".join([f"{k} = {v}" for k, v in data["stats"].items()]))
        return ""

    else:
        return data["stats"]

async def endpoints(json=False):
    data = await HTTPClient().get_url_json(f"{__url__}/api") 
    endpoints = "\n".join([f"GET {i}" for i in data["endpoints"]])

    if not json:
        print(f"Base URL: {__url__}\n\nEndpoints:\n\n{endpoints}")
        return ""
        
    else:
        return data