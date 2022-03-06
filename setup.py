from setuptools import setup, find_packages
 
VERSION = '0.0.2'
DESCRIPTION = "An asynchronous (badly coded) wrapper for FusionSidAPI."

setup(
    name='fusionsidsapi',
    version=VERSION,
    author='Siddhesh Zantye',
    author_email='siddheshadsv@icloud.com',
    url='https://github.com/FusionSid/FusionSidsAPI',
    description=DESCRIPTION,
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        "aiohttp==3.8.1",
        "aiofiles==0.6.0"
    ]
)

# python3 setup.py bdist_wheel
# twine upload dist/*
# twine upload --skip-existing dist/*
# sudo rm -rf ./build ./dist ./*egg-info