# -- Project information -----------------------------------------------------
project = 'HP Printer Setup Guide'
author = 'Your Name'
release = '1.0'

# -- General configuration ---------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Sphinx extensions to use
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

# Path to templates
templates_path = ['_templates']

# Exclude patterns
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'furo'  # Use the Furo theme, assuming it has been installed via pip
html_theme_options = {
    'sidebar_hideindex': False,
    'navigation_with_keys': True,
}

# Paths for static files (e.g., CSS, images)
html_static_path = ['_static']

# Custom CSS file to apply custom styles
html_css_files = ['_static/custom.css']

# -- Options for HTMLHelp output -------------------------------------------
htmlhelp_basename = 'HPPrinterSetupGuide'

# -- Options for LaTeX output ----------------------------------------------
latex_documents = [
    ('index', 'HPPrinterSetupGuide.tex', 'HP Printer Setup Guide Documentation',
     'Your Name', 'manual'),
]

# -- Options for manual page output ---------------------------------------
man_pages = [
    ('index', 'hpprintersetupguide', 'HP Printer Setup Guide Documentation',
     [author], 1)
]

# -- Options for Texinfo output --------------------------------------------
texinfo_documents = [
    ('index', 'HPPrinterSetupGuide', 'HP Printer Setup Guide Documentation',
     author, 'HPPrinterSetupGuide', 'One line description of project.',
     'Miscellaneous'),
]

# -- Options for ePub output ----------------------------------------------
epub_title = project
epub_author = author
epub_publisher = author
epub_identifier = 'http://example.com/HpPrinterSetupGuide'
epub_exclude_files = ['search.html']
