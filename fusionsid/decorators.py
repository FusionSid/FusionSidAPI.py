import functools
from .fun import Fun


class Decorators:
    @classmethod
    def compliment(cls, *args, **kwargs):
        """
        Compliment Decorator
        Putting this above a function will print a compliment before the function is run

        Example:
        --------
        ```

        compliment = Decorators.compliment

        @compliment()
        async def main():
            pass
        ```

        """

        def wrapper(func):
            @functools.wraps(func)
            async def wrapped(*args, **kwargs):
                print((await Fun.compliment()))
                return await func(*args, **kwargs)

            return wrapped

        return wrapper

    @classmethod
    def fact(cls, *args, **kwargs):
        """
        Fact Decorator
        Putting this above a function will print a fact before the function is run

        Example:
        --------
        ```

        fact = Decorators.fact

        @fact()
        async def main():
            pass
        ```

        """

        def wrapper(func):
            @functools.wraps(func)
            async def wrapped(*args, **kwargs):
                print((await Fun().fact()))
                return await func(*args, **kwargs)

            return wrapped

        return wrapper

    @classmethod
    def roast(cls, *args, **kwargs):
        """
        Roast Decorator
        Putting this above a function will print a roast before the function is run

        Example:
        --------
        ```

        roast = Decorators.roast

        @roast()
        async def main():
            pass
        ```

        """

        def wrapper(func):
            @functools.wraps(func)
            async def wrapped(*args, **kwargs):
                print((await Fun.roast()))
                return await func(*args, **kwargs)

            return wrapped

        return wrapper

    @classmethod
    def truth(cls, *args, **kwargs):
        """
        Truth Decorator
        Putting this above a function will print a truth before the function is run

        Example:
        --------
        ```

        truth = Decorators.truth

        @truth()
        async def main():
            pass
        ```

        """

        def wrapper(func):
            @functools.wraps(func)
            async def wrapped(*args, **kwargs):
                print((await Fun().truth()))
                return await func(*args, **kwargs)

            return wrapped

        return wrapper

    @classmethod
    def dare(cls, *args, **kwargs):
        """
        Dare Decorator
        Putting this above a function will print a dare before the function is run

        Example:
        --------
        ```

        dare = Decorators.dare

        @dare()
        async def main():
            pass
        ```

        """

        def wrapper(func):
            @functools.wraps(func)
            async def wrapped(*args, **kwargs):
                print((await Fun().dare()))
                return await func(*args, **kwargs)

            return wrapped

        return wrapper
