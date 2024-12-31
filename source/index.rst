.. documentation_tut documentation master file, created by
   sphinx-quickstart on Tue Dec 31 09:29:08 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the documentation_tut Using Sphinx and Read the Docs
===============================================================

Sphinx is a powerful documentation generator that is widely used for Python projects. It takes reStructuredText (reST) files and converts them into various output formats such as HTML, LaTeX, and ePub.

.. note::
    You can read more about Sphinx in the `official documentation <https://www.sphinx-doc.org/en/master/>`_.

Usage
-----

To start using Sphinx, you can create a basic configuration by running:

.. code-block:: bash
    sphinx-quickstart

This command sets up the initial directory structure for your documentation project.

reStructuredText
----------------

reStructuredText (reST) is a lightweight markup language that is the standard for Sphinx. It allows you to format text, create headings, lists, tables, and much more.

Some common syntax:

1. **Headings**: Use equals signs `=` for top-level headings, dashes `-` for second-level headings, etc.

Example:

.. code-block:: rst
    Top-Level Heading
    ==================
    
    Second-Level Heading
    ----------------------

2. **Bold Text**: Use double asterisks for bold text.
    
    Example: ``**This is bold text**``

3. **Lists**: Use asterisks `*` or hyphens `-` for unordered lists.
    
    Example:
    
    * Item 1
    * Item 2

For more detailed information, visit the `reStructuredText documentation <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_.

``Read the Docs``
-----------------

Read the Docs is an excellent service for hosting and building Sphinx-based documentation. It integrates seamlessly with Git repositories and automatically rebuilds your documentation when changes are detected.

Learn more at `Read the Docs <https://readthedocs.org/>`_.


.. toctree::
   :maxdepth: 5
   :caption: Contents:

   test
   mermaid
   grid_table
   simple_table
   image