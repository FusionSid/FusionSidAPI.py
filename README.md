[![CodeFactor](https://www.codefactor.io/repository/github/fusionsid/fusionsidapi.py/badge)](https://www.codefactor.io/repository/github/fusionsid/fusionsidapi.py)

# FusionSidAPI Wrapper for python

An asynchronous (badly coded) api wrapper to use [FusionSidAPI](https://fusionsidapi.herokuapp.com/) in python.

---

# Install:

You can install this library from PyPi: [Link](https://pypi.org/project/fusionsidsapi/)

**Install with pip:**
```py
pip install fusionsidsapi
```

---

# Examples:

Look in the [examples](/examples/) folder for some examples

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