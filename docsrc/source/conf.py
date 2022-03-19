import os
import sys

sys.path.insert(0, os.path.abspath('..'))

from fusionsid import *

project = 'FusionSidAPI.py'
copyright = '2022, Siddhesh Zantye'
author = 'Siddhesh Zantye'

release = '0.0.8'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']