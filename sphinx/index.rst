.. pyFlightscript documentation master file, created by
   sphinx-quickstart on Thu Jul 24 00:14:01 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pyFlightscript Documentation
============================

A Python API for generating native FlightStream solver scripts with a focus on ease of use and robustness.

.. note::
   This library is compatible with **FlightStream 2025.1** and later.

Getting Started
===============

Installation
------------

Install the library directly from GitHub using pip:

.. code-block:: bash

   pip install git+https://github.com/altairengineering/pyFlightscript.git

Quick Start Example
-------------------

Here is a basic example of how to use ``pyFlightscript``:

.. code-block:: python

   import pyFlightscript as pyfs

   # 1. Define the path to your FlightStream executable
   fsexe_path = r'C:\path\to\your\FlightStream.exe'

   # 2. (Optional) Clear any previous script state from memory
   pyfs.script.hard_reset()

   # 3. Use pyFlightscript functions to build your script commands
   pyfs.open_fsm(fsm_filepath="path/to/your/model.fsm")
   pyfs.solver.initialize_solver(solver_model="INCOMPRESSIBLE", surfaces=-1)
   pyfs.exec_solver.start_solver()
   pyfs.close_flightstream()

   # 4. Write and execute the script
   pyfs.write_to_file() # write the script to script_out.txt
   pyfs.execute_fsm_script(fsexe_path=fsexe_path, hidden=True) # optional, can also run from GUI

Key Features
============

* **Pythonic Interface:** Write clean, readable Python code that generates complex FlightStream scripts
* **Organized Modules:** Functions are grouped into logical modules for easy discovery
* **Static Type Checking:** Fully type-hinted codebase helps catch errors early
* **Direct Execution:** Execute generated scripts directly from Python

API Reference
=============

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
