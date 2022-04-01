from .http import HTTPClient
from typing import Dict


class Text:
    """
    A bunch of Text functions
    -------------------------

    Methods
    -------
        text_to_binary(text : str) : Converts text to binary

        text_to_hex(text : str) : Converts text to hex

        binary_to_text(binary : str) : Converts binary to text

        hex_to_text(hex : str) : Converts hex to text

        hash(text : str) : Hashes text

        password(text : str, length : str = None) : Generates a password

        expand(text : str) : Expands Text

        drunkify(text : str) : Drunkifies Text

        reverse(text : str) : Reverses Text

    """

    @classmethod
    async def text_to_binary(cls, text: str) -> Dict:
        """
        Parameters
        ----------
            :param text (str) : The text you want to convert

        Example
        -------
            >>> print(await Text.text_to_binary(text="Hello"))
        """

        data = await HTTPClient().get_json(f"""texttobinary?text={text}""")

        return data["binary"]

    @classmethod
    async def text_to_hex(cls, text: str) -> Dict:
        """
        Parameters
        -----
            :param text (str) : The text you want to convert

        Example
        -------
            >>> print(await Text.text_to_hex(text="Hello"))
        """
        data = await HTTPClient().get_json(f"""texttohex?text={text}""")

        return data["hex"]

    @classmethod
    async def binary_to_text(cls, binary: str) -> Dict:
        """
        Parameters
            :param binary (str) : The binary you want to convert to text

        Example
        -------
            >>> print(await Text.text_to_binary(binary=""))
        """
        data = await HTTPClient().get_json(f"""binarytotext?binary_text={binary}""")

        return data["text"]

    @classmethod
    async def hex_to_text(cls, hex: str) -> Dict:
        """
        Parameters
            :param hex (str) : The hex you want to convert to text

        Example
        -------
            >>> print(await Text.hext_to_text(hex=""))
        """
        data = await HTTPClient().get_json(f"""hextotext?hex_text={hex}""")

        return data["text"]

    @classmethod
    async def hash(cls, text: str) -> Dict:
        """
        Parameters
        -----
            :param text (str) : The text you want to hash

        Example
        -------
            >>> print(await Text.hash(text="Hello"))
        """
        data = await HTTPClient().get_json(f"""encrypt?text={text}""")

        return data["encrypted"]

    @classmethod
    async def password(cls, text: str, length: int = 8) -> Dict:
        """
        Parameters
        -----
            :param text (str) : The text you want to convert
            :param length (int Optional) : The length of the password

        Example
        -------
            >>> print(await Text.password(text="Hello", length=8))
        """
        data = await HTTPClient().get_json(f"""password?text={text}?length={length}""")

        return data["password"]

    @classmethod
    async def expand(cls, text: str, space: int = 5) -> Dict:
        """
        Parameters
        -----
            :param text (str) : The text you want to convert
            :param space (str Optional) : The space between each letter

        Example
        -------
            >>> print(await Text.expand(text="Hello", space=5))
        """
        data = await HTTPClient().get_json(f"""expand?text={text}?space={space}""")

        return data["text"]

    @classmethod
    async def reverse(cls, text: str) -> Dict:
        """
        Parameters
        -----
            :param text (str) : The text you want to convert

        Example
        -------
            >>> print(await Text.reverse(text="Hello"))
        """
        data = await HTTPClient().get_json(f"""reverse?text={text}""")

        return data["text"]

    @classmethod
    async def drunkify(cls, text: str) -> Dict:
        """
        Parameters
        -----
            :param text (str) : The text you want to convert

        Example
        -------
            >>> print(await Text.drunkify(text="Hello"))
        """

        data = await HTTPClient().get_json(f"""drunkify?text={text}""")

        return data["text"]
