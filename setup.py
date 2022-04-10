from setuptools import setup, find_packages
from fusionsid import __version__, __author__, __github__

DESCRIPTION = "An asynchronous api wrapper for FusionSidsAPI."
LONG_DESCRIPTION = open("README.md").read() + "\n\n" + open("CHANGELOG.txt").read()

setup(
    name="fusionsidsapi",
    version=__version__,
    author=__author__,
    author_email="siddheshadsv@icloud.com",
    url=__github__,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "aiofiles==0.6.0",
        "aiohttp==3.8.1",
        "Pillow==9.1.0",
        "rich==12.2.0",
    ],
    entry_points={"console_scripts": ["fusionsid=fusionsid.__main__:main"]},
)

# python3 setup.py bdist_wheel
# twine upload dist/*
# twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
# rm -rf ./build ./dist ./*egg-info
