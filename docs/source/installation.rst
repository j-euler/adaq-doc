============
Installation
============

ADAQ requires a local installation, ideally in a location where the data does not have to be moved later.
For example, an interfaceable storage archive.

.. _httk:

The High-Throughput Toolkit (*httk*)
=============

More info about *httk*, see https://docs.httk.org/en/latest/.

**Install httk**

Install the `devel`_ branch by following the instructions here: 

.. _devel: https://github.com/httk/httk/tree/devel

.. code-block:: console

   $ git clone -b devel https://github.com/httk/httk.git

Ensure to use the *devel* branch.

**Configure httk**

*httk* uses other software to find symmetry and show crystal structures:

* isotropy (required for ADAQ)
* jmol (optional but recommended)

Place the isotropy files where you want and edit *isotropy/findsym* to find the absolute path:

.. code-block:: console

   export ISODATA=/path/to/isotropy/iso-9.3.1/
   exec /path/to/isotropy/iso-9.3.1/findsym "$@"

Place jmol files where you want.

In the httk folder, run:

.. code-block:: console

   cp httk.cfg.example src/httk/httk.cfg
   
Edit the paths in *src/httk/httk.cfg* to link to isotropy and jmol (absoulute path):

.. code-block:: console

   isotropy=/path/to/isotropy
   jmol=/path/to/jmol-14.4.0_2015.10.22b/jmol.sh

.. _ADAQ:

ADAQ
=============
   
**Install ADAQ**

Clone the directory from github:

.. code-block:: console

   $ git clone <link to ADAQ when public>

The current version of ADAQ runs with python 2.7 and requires the python package tess.
A suggestion is to make a virtualenv or conda with python 2.7 and tess:

.. code-block:: console

   $ conda create -n adaq python=2.7

activate this environment with:

.. code-block:: console

   $ conda activate adaq

and install `tess`_ with:

.. code-block:: console

   (adaq) $ pip install --user tess

.. _tess: https://github.com/wackywendell/tess

**Test installation**

Ensure to source *httk* and ADAQ as well as activate the conda environment:

.. code-block:: console

   $ source /path/to/httk/init.shell
   $ source /path/to/ADAQ/init.shell
   $ conda activate adaq

In the ADAQ folder, run:

.. code-block:: console

   (adaq) $ python test_installation.py

If you want to test with jmol, run:

.. code-block:: console

   (adaq) $ python test_installation.py jmol

   
.. _supercomputer:

Supercomputer
=============

ADAQ and *httk* interfaces with a supercomputer to do the calculations.
At the supercomputer, you require `VASP`_ and a python installation with numpy and scipy.

.. _VASP: https://www.vasp.at/

.. _LiU:

Linköping University specifics
------------------------------

Recommended to install httk and ADAQ at `dedur01`.
At dedur01, the required files are located here:

* istropy (/dedur01/data/shared/httk_libs/isotropy)
* jmol (/dedur01/data/shared/httk_libs/jmol/jmol-14.4.0_2015.10.22b/jmol.sh)

.. note::
   
   At dedur, you may need to install gcc compiler. use the following command: ``conda install compilers`

It is also recommended to add configure ssh connection sharing at dedur.
Add the following code to ``.ssh/config``:

.. code-block:: console

   Host tetralith.nsc.liu.se
   User x_abcde
   ControlMaster auto
   ControlPath ~/.ssh/cm-%r@%h:%p
   ControlPersist 8h

When using tetralith or sigma, install a conda environment:

.. code-block:: console

   $ conda create -n adaq2 python=2.7 numpy scipy


.. _dedur01: https://gitlab.liu.se/theophys/guide/-/wikis/Computing/dedur01
