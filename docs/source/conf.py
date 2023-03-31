# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'bikeshare'
copyright = '2023, jay'
author = 'jay'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.duration",
    "sphinx.ext.autosectionlabel",
    
]

myst_enable_extensions = [
    "dollarmath"
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import sphinx_rtd_theme
#html_theme = 'sphinx_rtd_theme'
html_theme = 'furo'

#html_theme = 'alabaster'

# the following function is optional
def setup(app):
    app.add_css_file('my_theme.css')

html_static_path = ['_static']
