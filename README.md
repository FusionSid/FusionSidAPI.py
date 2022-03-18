[![CodeFactor](https://img.shields.io/codefactor/grade/github/FusionSid/FusionSidAPI.py?style=for-the-badge)](https://www.codefactor.io/repository/github/fusionsid/fusionsidapi.py)
[![Downloads](https://img.shields.io/pypi/dd/fusionsidsapi?style=for-the-badge)](https://pypi.org/project/fusionsidsapi/)
[![PyPi-Version](https://img.shields.io/pypi/v/fusionsidsapi?style=for-the-badge)](https://pypi.org/project/fusionsidsapi/)


# FusionSidAPI Wrapper for python

An asynchronous api wrapper to use [FusionSidAPI](https://fusionsidapi.herokuapp.com/) in python.

---

# Install:

You can install this library from PyPi: [Link](https://pypi.org/project/fusionsidsapi/)

**Install with pip:**
```py
pip install fusionsidsapi
```

---

# Need Help

Even though there is so documentation for this package at the moment, each class and function has a doc string so if you need help with anything in the pacakge just use the built in python function `help()`

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
    roast = await Fun().roast()
    print(roast)

loop = asyncio.new_event_loop()
loop.run_until_complete(main())
```

---

### [FusionSidAPI Github](https://github.com/FusionSid/FusionSidsAPI)

---

## Contact:
Discord: `FusionSid#3645`

[My Github](https://github.com/FusionSid/)

## Changelog:
You can checkout the changes per version in [CHANGELOG.txt](https://github.com/FusionSid/FusionSidAPI.py/blob/master/CHANGELOG.txt)
