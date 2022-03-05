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

async def stats():
    data = await HTTPClient().get_url_json(f"{__url__}/stats")
    print("\n".join([f"{k} = {v}" for k, v in data["stats"].items()]))
    return data["stats"]