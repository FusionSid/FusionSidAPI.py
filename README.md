[![CodeFactor](https://img.shields.io/codefactor/grade/github/FusionSid/FusionSidAPI.py?style=for-the-badge)](https://www.codefactor.io/repository/github/fusionsid/fusionsidapi.py)
[![Downloads](https://img.shields.io/pypi/dd/fusionsidsapi?style=for-the-badge)](https://pypi.org/project/fusionsidsapi/)
[![PyPi-Version](https://img.shields.io/pypi/v/fusionsidsapi?style=for-the-badge)](https://pypi.org/project/fusionsidsapi/)


# FusionSidAPI Wrapper for python

An asynchronous api wrapper to use [FusionSidAPI](https://fusionsidapi.herokuapp.com/) in python.

[Docs url](https://fusionsid.github.io/FusionSidAPI.py/)

---

# Install:

You can install this library from PyPi: [Link](https://pypi.org/project/fusionsidsapi/)

**Install with pip:**
```py
pip install fusionsidsapi
```

---

# Need Help

### Docs
This package has [docs](https://fusionsid.github.io/FusionSidAPI.py/)

Go to this url
https://fusionsid.github.io/FusionSidAPI.py/  
or look in the Enviroments tab for the latest github pages deployment

### Help Function
Each class and function has a doc string so if you need help with anything in the pacakge just use the built in python function `help()`

eg:
```py
import fusionsid

# Example 1
help(fusionsid.RandomMeme)
help(fusionsid.GenerateMeme)

# Example 2
help(fusionsid.Image.qrcode)
help(fusionsid.Fun.truth_or_dare)

```

# Examples:

Look in the [examples](https://github.com/FusionSid/FusionSidAPI.py/tree/master/examples) folder for some examples

Example for getting a roast:
```py
import asyncio
from fusionsid import Fun

async def main():
    roast = await Fun.roast()
    print(roast)

loop = asyncio.new_event_loop()
loop.run_until_complete(main())
```

This package also has some decorators (also in the [examples](https://github.com/FusionSid/FusionSidAPI.py/tree/master/examples) folder) so if you want a complement before your code is run heres how:
```py
import asyncio
from fusionsid import Decorators

do_compliment = Decorators.compliment

@do_compliment()
async def main():
    print("Wassup")

loop = asyncio.new_event_loop()
loop.run_until_complete(main())
```

---

### [FusionSidAPI Github](https://github.com/FusionSid/FusionSidsAPI)

---

### CLI Tool

Typing `fusionsid` in terminal or `python3 -m fusionsid` will bring up the mini cli thing i made for this module.

It can let you use the api in terminal in a fast and easy way.

**Use:** `fusionsid --help` or `python3 -m fusionsid --help` for help

---

## Changelog:
You can checkout the changes per version in [CHANGELOG.txt](https://github.com/FusionSid/FusionSidAPI.py/blob/master/CHANGELOG.txt)


---

## Contact:

If you find a bug please make an issue, I will try my best to fix it :)

Discord: `FusionSid#3645` [My Github](https://github.com/FusionSid/)

---