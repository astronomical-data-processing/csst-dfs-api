.. CSST DFS API documentation master file, created by
   sphinx-quickstart on Thu Jun 10 08:55:39 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to CSST DFS API's documentation!
========================================

This package provides APIs to access CSST's files and databases.

Installation
================

This library can be installed with the following command: 

.. code-block:: c

   git clone https://github.com/astronomical-data-processing/csst-dfs-api.git
   cd csst-dfs-api
   pip install -r requirements.txt
   python setup.py install 

* NOTE: This library is heavily under coding, if any bugs occur, firstly you should try to update codes and install again like:

.. code-block:: c

   git pull
   pip install -r requirements.txt
   python setup.py install 

Documentation for the Code
**************************
.. toctree::
   :maxdepth: 2
   :caption: Contents:

Common
=====================
.. automodule:: csst_dfs_api.common
   :members:

Facility
=======================
.. automodule:: csst_dfs_api.facility
   :members:

MSC
=======================
.. automodule:: csst_dfs_api.msc
   :members:

IFS
=======================
.. automodule:: csst_dfs_api.ifs
   :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

