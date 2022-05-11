# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme
import myst_parser
import os

# -- Project information -----------------------------------------------------

project = 'RHoMIS'
copyright = '2021, Léo Gorman'
author = 'Léo Gorman'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    "myst_parser",
    'sphinxcontrib.youtube'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['drafts','_build', 'Thumbs.db', '.DS_Store','env/*',
                    'README.md', 'copy_diagramns.sh', "source/utils/links-production.rst", 
                    "source/utils/links-staging.rst"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']
html_static_path = []

html_theme_options = {
    'prev_next_buttons_location': 'both'
}



# Need to specify suffixes so it knows which files to look for
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}


# make rst_epilog a variable, so you can add other epilog parts to it
rst_epilog =""
# Read link all targets from file

docenv = os.getenv("DOCENV")
if (docenv=="production"):
    links_file="./source/utils/links-production.rst"
elif (docenv=="staging"):
    links_file="./source/utils/links-staging.rst"
else:
    raise ValueError("""

    Did not specify whether staging or production environment.
    Please include DOCENV=staging or DOCENV=production in your
    command""")


print("docenv")
print(docenv)

with open(links_file) as f:
     rst_epilog += f.read()

print(rst_epilog)