import functools
from .fun import Fun

class Decorators:

    @classmethod
    def compliment(cls, *args, **kwargs):
        def wrapper(func):
            @functools.wraps(func)
            async def wrapped(*args, **kwargs):
                print((await Fun.compliment()))
                return await func(*args, **kwargs)
            return wrapped
        return wrapper


    @classmethod
    def fact(cls, *args, **kwargs):
        def wrapper(func):
            @functools.wraps(func)
            async def wrapped(*args, **kwargs):
                print((await Fun().fact()))
                return await func(*args, **kwargs)
            return wrapped
        return wrapper


    @classmethod
    def roast(cls, *args, **kwargs):
        def wrapper(func):
            @functools.wraps(func)
            async def wrapped(*args, **kwargs):
                print((await Fun.roast()))
                return await func(*args, **kwargs)
            return wrapped
        return wrapper


    @classmethod
    def truth(cls, *args, **kwargs):
        def wrapper(func):
            @functools.wraps(func)
            async def wrapped(*args, **kwargs):
                print((await Fun().truth()))
                return await func(*args, **kwargs)
            return wrapped
        return wrapper


    @classmethod
    def dare(cls, *args, **kwargs):
        def wrapper(func):
            @functools.wraps(func)
            async def wrapped(*args, **kwargs):
                print((await Fun().dare()))
                return await func(*args, **kwargs)
            return wrapped
        return wrapper