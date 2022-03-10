from .http import HTTPClient
from typing import Dict
from .errors import *


class Text():
    """
    A bunch of Text functions
    ----

    Methods
    -------
        text_to_binary(text : str) : Converts text to binary

        text_to_hex(text : str) : Converts text to hex

        binary_to_text(binary : str) : Converts binary to text

        hex_to_text(hex : str) : Converts hex to text
        
        encrypt(text : str) : Encrypts text (Can not be decrypted)

        password(text : str, length : str = None) : Generates a password

        expand(text : str) : Expands Text

        drunkify(text : str) : Drunkifies Text

        reverse(text : str) : Reverses Text
        
    """

    async def text_to_binary(self, text : str) -> Dict:
        """
        Args
        -----
            text (str) : The text you want to convert

        Example
        -------
            >>> print(await Text().text_to_binary(text="Hello"))
        """

        data = await HTTPClient().get_json(f"""texttobinary?text={text}""")

        return data["binary"]


    async def text_to_hex(self, text : str) -> Dict:
        """
        Args
        -----
            text (str) : The text you want to convert

        Example
        -------
            >>> print(await Text().text_to_hex(text="Hello"))
        """
        data = await HTTPClient().get_json(f"""texttohex?text={text}""")
        
        return data["hex"]


    async def binary_to_text(self, binary : str) -> Dict:
        """
        Args:
            binary (str) : The binary you want to convert to text

        Example
        -------
            >>> print(await Text().text_to_binary(binary=""))
        """
        data = await HTTPClient().get_json(f"""binarytotext?binary_text={binary}""")
        
        return data["text"]


    async def hex_to_text(self, hex : str) -> Dict:
        """
        Args:
            hex (str) : The hex you want to convert to text

        Example
        -------
            >>> print(await Text().hext_to_text(hex=""))
        """
        data = await HTTPClient().get_json(f"""hextotext?hex_text={hex}""")

        return data["text"]
    

    async def encrypt(self, text : str) -> Dict:
        """
        Args
        -----
            text (str) : The text you want to convert

        Example
        -------
            >>> print(await Text().encrypt(text="Hello"))
        """
        data = await HTTPClient().get_json(f"""encrypt?text={text}""")
        
        return data["encrypted"]
    

    async def password(self, text : str, length : int = 8) -> Dict:
        """
        Args
        -----
            text (str) : The text you want to convert
            length (int Optional) : The length of the password

        Example
        -------
            >>> print(await Text().password(text="Hello", length=8))
        """
        data = await HTTPClient().get_json(f"""password?text={text}?length={length}""")

        return data["password"]
    

    async def expand(self, text : str, space : int = 5) -> Dict:
        """
        Args
        -----
            text (str) : The text you want to convert
            space (str Optional) : The space between each letter
            
        Example
        -------
            >>> print(await Text().expand(text="Hello", space=5))
        """
        data = await HTTPClient().get_json(f"""expand?text={text}?space={space}""")

        return data["text"]
    
    
    async def reverse(self, text : str) -> Dict:
        """
        Args
        -----
            text (str) : The text you want to convert

        Example
        -------
            >>> print(await Text().reverse(text="Hello"))
        """
        data = await HTTPClient().get_json(f"""reverse?text={text}""")

        return data["text"]

    
    async def drunkify(self, text : str) -> Dict:
        """
        Args
        -----
            text (str) : The text you want to convert

        Example
        -------
            >>> print(await Text().drunkify(text="Hello"))
        """
    
        data = await HTTPClient().get_json(f"""drunkify?text={text}""")

        return data["text"]
    

    
