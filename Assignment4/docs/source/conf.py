import os
import sys
sys.path.insert(0, os.path.abspath('../../app'))

# -- Project information -----------------------------------------------------
project = 'taskmanager'
copyright = '2025, nikolas'
author = 'nikolas'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []




html_theme = 'alabaster'
html_static_path = ['_static']
