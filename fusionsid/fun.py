from .http import HTTPClient
from typing import Dict, List
from .errors import *

class Fun():
    """
    A bunch of Fun functions
    ----

    Methods
    -------
        eightball() : 8ball
        roast() : Returns a roast
        compliment() : Returns a complement
        truth() : Returns a truth
        dare() : Returns a dare
        truth_or_dare() : Returns a Dict with a truth, dare and random choice
        fact() : Returns a fact
        wordle() : Gets the wordle answer for today
        reddit_search(keyword : str) : Searches reddit
    """

    async def eightball(self) -> str:
        """
        Example
        -------
            >>> print(await Fun().eightball())
        """
        data = await HTTPClient().get_json("8ball")
        return data["answer"]
    
    async def roast(self) -> str:
        """
        Example
        -------
            >>> print(await Fun().roast())
        """
        data = await HTTPClient().get_json("roast")
        return data["roast"]
    
    async def compliment(self) -> str:
        """
        Example
        -------
            >>> print(await Fun().compliment())
        """
        data = await HTTPClient().get_json("compliment")
        return data["compliment"]

    async def truth(self) -> str:
        """
        Example
        -------
            >>> print(await Fun().truth())
        """
        data = await HTTPClient().get_json("truthordare")
        return data["truth"]

    async def dare(self) -> str:
        """
        Example
        -------
            >>> print(await Fun().dare())
        """
        data = await HTTPClient().get_json("truthordare")
        return data["dare"]
    
    async def truth_or_dare(self) -> Dict[str, str]:
        """
        Example
        -------
            >>> print(await Fun().truth_or_dare())
        """
        data = await HTTPClient().get_json("truthordare")
        return data

    async def fact(self) -> str:
        """
        Example
        -------
            >>> print(await Fun().fact())
        """
        data = await HTTPClient().get_json("fact")
        return data["fact"]

    async def wordle(self) -> str:
        """
        Example
        -------
            >>> print(await Fun().wordle())
        """
        data = await HTTPClient().get_json("wordle")
        return data["wordle"]

    async def reddit_search(self, keyword : str) -> List[Dict]:
        """
        Args:
            keyword (str) : The search query to search on reddit

        Example
        -------
            >>> print(await Fun().reddit_search(keyword="Meme"))
        """
        data = await HTTPClient().get_json(f"""searchreddit?keyword={keyword}""")
        
        return data