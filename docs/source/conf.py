# Configuration file for the Sphinx documentation builder.
# This file only contains a selection of the most common options.
# For a full list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# -- Path setup --------------------------------------------------------------
# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('../src'))  # Adjust as needed

# -- Project information -----------------------------------------------------

project = 'Setup HP printer'
copyright = '2025, Setup HP printer'
author = 'Setup HP printer'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- Google site verification ------------------------------------------------
def add_google_verification(app, pagename, templatename, context, doctree):
    context['google_verification'] = '''
    <meta name="google-site-verification" content="fL4pdqYIa6vMjXlU0Q6XLuzxD2ZBar5O7O6aaVIQI4Q" />
    '''
    return context

# -- Favicon ---------------------------------------------------------------
html_favicon = 'favicon.ico'  # Make sure your favicon.ico file is in the static directory

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings.
# These extensions are optional but useful for Read the Docs.
# extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.viewcode']

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
# Use the Read the Docs theme for better compatibility with Read the Docs.
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets)
# here, relative to this directory. These files are copied after the built-in
# static files, so a file named "default.css" will overwrite the built-in one.
html_static_path = ['_static']

# -- Options for HTML output -------------------------------------------------

# Hide "View page source" link and copyright
html_show_sourcelink = False
html_show_copyright = False

# Customize the theme options
html_theme_options = {
    'show_powered_by': False,  # Disable "Powered by Sphinx"
}

# Hook to add the Google verification meta tag to every page
def setup(app):
    app.connect('html-page-context', add_google_verification)
