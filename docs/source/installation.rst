Installation
=====

.. _installation:

Installation
------------

ADAQ requires a local installation, ideally in a location where the data does not have to be moved later.
For example, a interfacable storage archive.

.. _httk:

*httk*
------

More info about *httk*, see `https://docs.httk.org/en/latest/`.

**Install httk**

You need to install The High-Throughput Toolkit (httk).
Install the `devel`_ branch by following the instructions here: 

.. _devel: https://github.com/httk/httk/tree/devel

.. code-block:: console

   $ git clone https://github.com/httk/httk.git

Change to *devel* branch

**configure httk with isotrpy and jmol**

httk uses other softwares to find symmetry and show crystal structures:
isotropy (required for ADAQ)
jmol (optional but recommended)

Place the isotropy files where you want and edit isotropy/findsym find the absoulute path:
.. code-block:: console

   export ISODATA=/path/to/isotropy/iso-9.3.1/
   exec /path/to/isotropy/iso-9.3.1/findsym "$@"

Place jmol files where you want

In the httk folder, run:
.. code-block:: console

   cp httk.cfg.example src/httk/httk.cfg
   
Edit the path in httk.cfg to link to isotropy and jmol (absoulute path):
.. code-block:: console

   isotropy=/path/to/isotropy
   jmol=/path/to/jmol-14.4.0_2015.10.22b/jmol.sh

.. _ADAQ:

ADAQ
----
   
**Install ADAQ**

Clone the directory from github:
.. code-block:: console

   $ git clone <link to ADAQ when public>

The current version of ADAQ runs with python 2.7 and requires the python package tess.
A suggestion is to make a virtualenv or conda with python 2.7 and tess:
.. code-block:: console

   conda create -n adaq python=2.7 tess

activate this enviroment with:
.. code-block:: console

   conda activate adaq

**Test installation**

In the ADAQ folder, run:
.. code-block:: console

   (adaq) $ python test_installation.py

If you want to test with jmol, run:
.. code-block:: console

   (adaq) $ python test_installation.py jmol


.. _LiU:

Linköping Univserity specifics
------------------------------

recommended to use dedur01
