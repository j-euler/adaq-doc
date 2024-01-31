# Configuration file for the Sphinx documentation builder.

import os
import sys

sys.path.insert(0, os.path.abspath('.'))

# -- Project information

project = 'ADAQ-doc'
copyright = '2024, Davidsson'
author = 'Joel Davidsson'

release = '0.1'
#version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_favicon = 'favicon.png'

html_logo = 'ADAQ_logo_header.png'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
#    'style_nav_header_background': '#800000'
}

# -- Options for EPUB output
#epub_show_urls = 'footnote'
