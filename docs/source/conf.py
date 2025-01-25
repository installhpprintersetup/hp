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

# Google Analytics
html_context = {
    'google_analytics_id': 'G-HZ7YD4S9P9',  # Replace with your Google Analytics Tracking ID
}


# Add custom HTML code to the pages (Google Analytics Script)
def add_google_analytics(app, pagename, templatename, context, doctree):
    context['google_analytics'] = '''
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-HZ7YD4S9P9"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-HZ7YD4S9P9');
    </script>
    '''
    return context

# Connect the Google Analytics script to the HTML output
def setup(app):
    app.connect('html-page-context', add_google_analytics)


# Favicon
html_favicon = 'favicon.ico'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. 
# These extensions are optional but useful for Read the Docs.


# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
# Use the Read the Docs theme for better compatibility with Read the Docs.
# html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets)
# here, relative to this directory. These files are copied after the built-in
# static files, so a file named "default.css" will overwrite the built-in one.
# html_static_path = ['_static']

html_show_sourcelink = False  # Hides the "View page source" link
html_show_copyright = False
html_theme_options = {
    'show_powered_by': False,  # Disable "Powered by Sphinx"
}
