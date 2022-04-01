from .http import HTTPClient
from typing import Dict, List


class Fun:
    """
    A bunch of Fun functions
    ------------------------

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

    @classmethod
    async def eightball(cls) -> str:
        """
        Example
        -------
            >>> print(await Fun.eightball())
        """
        data = await HTTPClient().get_json("8ball")
        return data["answer"]

    @classmethod
    async def roast(cls) -> str:
        """
        Example
        -------
            >>> print(await Fun.roast())
        """
        data = await HTTPClient().get_json("roast")
        return data["roast"]

    @classmethod
    async def compliment(cls) -> str:
        """
        Example
        -------
            >>> print(await Fun.compliment())
        """
        data = await HTTPClient().get_json("compliment")
        return data["compliment"]

    @classmethod
    async def truth(cls) -> str:
        """
        Example
        -------
            >>> print(await Fun.truth())
        """
        data = await HTTPClient().get_json("truthordare")
        return data["truth"]

    @classmethod
    async def dare(cls) -> str:
        """
        Example
        -------
            >>> print(await Fun.dare())
        """
        data = await HTTPClient().get_json("truthordare")
        return data["dare"]

    @classmethod
    async def truth_or_dare(cls) -> Dict[str, str]:
        """
        Example
        -------
            >>> print(await Fun.truth_or_dare())
        """
        data = await HTTPClient().get_json("truthordare")
        return data

    @classmethod
    async def fact(cls) -> str:
        """
        Example
        -------
            >>> print(await Fun.fact())
        """
        data = await HTTPClient().get_json("fact")
        return data["fact"]

    @classmethod
    async def wordle(cls) -> str:
        """
        Example
        -------
            >>> print(await Fun.wordle())
        """
        data = await HTTPClient().get_json("wordle")
        return data["wordle"]

    @classmethod
    async def reddit_search(cls, keyword: str) -> List[Dict]:
        """
        Parameters
            :param keyword (str) : The search query to search on reddit

        Example
        -------
            >>> print(await Fun.reddit_search(keyword="Meme"))
        """
        data = await HTTPClient().get_json(f"""searchreddit?keyword={keyword}""")

        return data
