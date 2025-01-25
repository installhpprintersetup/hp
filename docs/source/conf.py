# -- Project information -----------------------------------------------------

project = 'HP Printer Setup Guide'  # Name of your project
author = 'Your Name'  # Author of the documentation
release = '1.0'  # Version of the project

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',       # Automatically generate documentation from docstrings
    'sphinx.ext.napoleon',      # Support for Google-style and NumPy-style docstrings
    'sphinx.ext.viewcode',      # Add links to view source code in the docs
]

templates_path = ['_templates']  # Path to your custom templates (if any)
exclude_patterns = []           # Patterns for files to exclude from the build

# -- Options for HTML output -------------------------------------------------

html_theme = 'furo'  # HTML theme, 'furo' is a modern theme, you can use 'sphinx_rtd_theme' or others
html_static_path = ['_static']  # Path to static files like images and custom CSS
html_css_files = ['custom.css']  # Path to custom CSS for styling the docs

# -- Options for LaTeX output -------------------------------------------------

latex_elements = {
    'papersize': 'a4paper',  # Define the paper size for LaTeX output
}

# -- Options for EPUB output -------------------------------------------------

epub_show_urls = 'footnote'  # Show URLs in footnotes for EPUB output
