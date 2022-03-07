from .http import HTTPClient
from typing import *
from .errors import *

class Fun():

    async def eightball(self):
        """
        ### Example:
            >>> print(await Fun().eightball())
        """
        data = await HTTPClient().get_json("8ball")
        return data["answer"]
    
    async def roast(self):
        """
        ### Example:
            >>> print(await Fun().roast())
        """
        data = await HTTPClient().get_json("roast")
        return data["roast"]
    
    async def compliment(self):
        """
        ### Example:
            >>> print(await Fun().compliment())
        """
        data = await HTTPClient().get_json("compliment")
        return data["compliment"]

    async def truth(self):
        """
        ### Example:
            >>> print(await Fun().truth())
        """
        data = await HTTPClient().get_json("truthordare")
        return data["truth"]

    async def dare(self):
        """
        ### Example:
            >>> print(await Fun().dare())
        """
        data = await HTTPClient().get_json("truthordare")
        return data["dare"]
    
    async def truth_or_dare(self):
        """
        ### Example:
            >>> print(await Fun().truth_or_dare())
        """
        data = await HTTPClient().get_json("truthordare")
        return data

    async def fact(self):
        """
        ### Example:
            >>> print(await Fun().fact())
        """
        data = await HTTPClient().get_json("fact")
        return data["fact"]