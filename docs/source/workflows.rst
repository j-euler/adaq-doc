============
Workflows
============

.. _general:


General
=============

This document presents the workflows that run on a supercomputer.
The following workflows are the standard workflows in ADAQ, presented in the order they are used.

* (``0_chemical_potential`` - this workflow calculates the chemical potentials for the elemental phase. This is already precalculated, hence one does not need to run this workflow.)
* ``1_unitcell`` - this workflow relaxes the unit cell.
* ``2_node_scaling`` - this workflow optimizes the number of nodes for the defect calculations.
* ``3_host_supercell``- this workflow calculates the properties needed from the host supercell.
* ``4_screen`` - this workflow relaxes defects with various charge states and calculates the most relevant properties for one excitation.
* ``5_full`` - this workflow calculates all excitations for a defect.

The workflows are found ``ADAQ/workflows``
Each workflow has a run.py, templete folder, and usually a ``adaq-workflow`` command that interfaces with it.
The parameters for run.py are processed in ``ht.instantiate.py``.

.. warning::
   Do not modify these workflows if you want to add the data to the ADAQ database.
   These workflows have been optimized to give useful data at a reasonable computational cost.
   Read this documentation carefully to understand what parameter each workflow can be modified with.
   For more information on how to calculate other properties, see the 'make your own workflow' section below.

There are also additional workflows, to add...

.. _Chemical potential:
Chemical Potential
=============

This workflow calculates the chemical potentials for the elemental phases with the PBE and HSE functional.
The results are stored in ``element_dict.save`` that comes with ADAQ.
Hence, one does not need to run this workflow, and it does not have a ``adaq-workflow`` command.

.. _unit cell:
Unit Cell Relaxation
=============

Command: ``adaq-workflow-relax-unitcell``, see :doc:`commands`.

This workflow relaxes the unit cell restarting as needed to ensure the volume change does not affect the basis set.
Currently, only the PBE functional is implemented.


.. _node scaling:
Node Scaling
=============

Command: ``adaq-workflow-node_scaling``, see :doc:`commands`.

This workflow runs the host supercell over a selected number of nodes and gives a scaling plot (saved at ``tuning\nodes_<computer name>.pdf``).
Here, the user will select how many nodes the remaining workflows will run with.
It also set the ``NBANDS`` vasp tag to be a number that is divible by the number of cores.
The results are ``ht.project/adaq``.
Note that this needs to be done for each computer.
Currently, only the PBE functional is implemented.

.. _host supercell:
Host Supercell
=============

Command: ``adaq-workflow-calculate-host``, see :doc:`commands`.

This workflow calculates the total energy for the screening and full workflow.
Currently, only the PBE functional is implemented.

.. _screen:
Screen
=============

Command: ``adaq-workflow-screen-defects``, see :doc:`commands`.

This workflow relaxes defects with various charge states.
The neutral charge state is always calculated.
Then, based on the ``charge`` tag, additional charge states are calculated.
As default, one negative (n1) and one positive (p1) charge state are calculated.
For each charge state, alternative spin states can be calculated.
Use the ``spin`` tag, true or false, to activate.
One excitation between defect states is calculated when possible for each charge and spin state.
ADAQ automatically finds localized defect states and calculates one excitation between them if the energy difference is large enough.
Excitations below the ``experimental_min_limit`` tag (default: 0.4 eV) are not calculated.

Currently, only the PBE functional is implemented.

To reduce the number of calculations, the screen workflow skips interstitial-interstitial cluster as default.

.. todo::
   add info on how to change the parameters.
   add references to adaq paper?


.. _full:
Full Charaterization
=============

Command: ``adaq-workflow-full``, see :doc:`commands`.

This workflow calculates all excitations for a defect with higher k-point grid.
It runs additional charge states, double negative and positive.

Currently, only the PBE functional is implemented.

.. _own workflow:
Make your own workflow
=============

.. todo::
   add later
