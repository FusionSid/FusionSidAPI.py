from setuptools import setup, find_packages
 
VERSION = '0.0.1'
DESCRIPTION = "An asynchronous (badly coded) wrapper for FusionSidAPI."

setup(
    name='sidspackage',
    version=VERSION,
    author='Siddhesh Zantye',
    author_email='siddheshadsv@icloud.com',
    url='https://github.com/FusionSid/FusionSidsAPI',
    description=DESCRIPTION,
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type='text/markdown',
    packages=find_packages()
)

# python3 setup.py bdist_wheel
# twine upload dist/*
# twine upload --skip-existing dist/*