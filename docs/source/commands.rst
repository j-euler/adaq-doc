============
Commands
============

.. _general:


General
=============

This document presents details about the ADAQ commands.
They are divide based on project, defect generation, workflow, and database.


.. _project:

Project
=============

Make an ADAQ project with the following command:

.. code-block:: console

   $ adaq-set-up-project

If you are uncertin of your progress, run the following command:

.. code-block:: console

   $ adaq-next-step

.. _defect:

Defect Generation
=============

To visualize any cell, use the following command:

.. code-block:: console

   $ adaq-show-cell <path>

where ``<path>`` is the path to the cell you would like to show, for example the relaxed unitcell (``/unitcell/ht.task.*.finished/ht.run.*/CONTCAR.relaxfinal.bz2``).

To generate defects, use the following command:

.. code-block:: console

   $ adaq-generate-defects

You can adjust the defect generation with the parameters in the ``parameter.py`` file.
It contains the following parameters:

* stacking_sequence - This is only relevant for layered material to keep track of with layer the different defect belong to. Leave as empty list for other materials.
* minimum_defect_distance - Set the minimum distance between defect clusters and periodic copies. Can also be viewed as the supercell size.  Given in `Å`ngstrom with default: 20.0
* vacancy - Generate vacancies, True or False.
* substitutional - Generate substitutionals, True or False.
* interstitial - Generate interstitials, True or False.
* dopand_string - Which elements to dope with. default: "intrinsic", one can also add "+" followed by the block in the peridoc table or write "all" for all dopants. It is also possible to specify a list of specific elements like "[Si,N]".
* only_single_dopands - Make only dopant cluster with single extrinsic element. If false, it is possible to make H and Li clusters in SiC. default: True
* cluster_size - How large defect clusters should be, default: 2
* min_distance - For defect clusters, provide the min pairwise defect distance in `Å`ngstrom, default: 1.0
* max_distance - For defect clusters, provide the max pairwise defect distance in `Å`ngstrom, default: 3.5
* int_distance - For interstitial generation, provide distance between interstitial positions in `Å`ngstrom, default: 0.5. Read more about this parameter below.

It can be tricky to set the number of interstital positions.
Hence, it can be tested before hand.
Test difference value of the ``int_distance`` in the ``parameter.py`` file and visualize the number of interstital position that are generated with the command:

.. code-block:: console

   $ adaq-show-interstitials-in-unitcell

.. todo::
   add example figures

.. _workflow:

Workflow
=============

Interface with the unitcell workflow:

.. code-block:: console

   $ adaq-workflow-relax-unitcell <arg1> <arg2> <arg3>
   
1st argument: ``setup, send, run, receive``
2nd argument: select which computer to run
3rd argument: number of taskmananger to run (optional)

Interface with the node scaling workflow:

.. code-block:: console

   $ adaq-workflow-node_scaling <arg1> <arg2> <arg3>
   
1st argument: ``run, status, collect, result``
2nd argument: select which computer to run
3rd argument: select number of nodes (default: 10, only needed for run argument)

Interface with the host workflow:

.. code-block:: console

   $ adaq-workflow-calculate-host <arg1> <arg2> <arg3>
   
1st argument: ``setup, send, run, receive``
2nd argument: select which computer to run
3rd argument: number of taskmananger to run (optional)

Interface with the screening workflow:

.. code-block:: console

   $ adaq-workflow-screen-defects <arg1> <arg2> <arg3>
   
1st argument: ``setup, send, run, receive``
2nd argument: select which computer to run
3rd argument: number of taskmananger to run (optional)

.. note::
   This workflow omits interstitial-interstitial cluster.
   To turn this off, go to ``ADAQ/workflows/4_screen/run.py`` and comment out ``search.add(~search_defectinfo.defect_name.like('%Int%Int%'))``

.. todo::
   Here is also possible to ristrict the number of defects in other ways, more on this later.
   how to interact with parameters for screen
   
Interface with the full workflow:

.. code-block:: console

   $ adaq-workflow-full <arg1> <arg2> <arg3>
   
1st argument: ``setup, send, run, receive``
2nd argument: select which computer to run
3rd argument: select which defect to run for setup or number of taskmananger to run (optional)


Interface with the lookup tables:

.. code-block:: console

   $ adaq-lookup <arg1> <arg2>
   
1st argument: select workflow, either ``screen`` or ``full``
2nd argument: select action, either ``display`` or ``rename``


.. _database:

Database
=============

.. todo::
   add automatic info about httk class in 
   mention sqlitebrower?

The following command goes through all data and makes the ``defects.sqlite`` database. 
It removes any older versions and make a new if the command is run again.

.. code-block:: console

   $ adaq-rebuild-database <arg1>
   
1st argument: select what to include in the database, either ``light`` (skips the relaxed defect structures) or ``full`` (default)

It is also possible to extract data from the the database.
To get a formation energy plot, run the following command:

.. code-block:: console

   $ adaq-database-plot-formation-energy <arg1>

1st argument: is the defect key, which is unique for the defect
.. todo::
   add save arguemnt?

To get a eigenvalues energy plot, run the following command:

.. code-block:: console

   $ adaq-database-plot-eigenvalues <arg1> <arg2> <arg3> <arg4>

1st argument: is the defect key, which is unique for the defect
2nd argument: select which workflow to extract the data from, ex: ``screen``
3rd argument: select which charge, ex: -1
4th argument: select which spin, ex: 1.0
5th argument: select which state, ``ground`` (default) or ``excited``

To show the defect cell, run the following command:

.. code-block:: console

   $ adaq-database-show-cell <arg1> <arg2> <arg3> <arg4>

1st argument: is the defect key, which is unique for the defect
2nd argument: select which workflow to extract the data from, ex: ``screen``
3rd argument: select which charge, ex: -1
4th argument: select which spin, ex: 1.0
5th argument: select which state, ``ground`` (default) or ``excited``

.. note::
   This command works even if the database is built with ``light`` since it access the relaxed files directly.

Get a copy of the defect cell, run the following command:

.. code-block:: console

   $ adaq-database-get-relaxed-structure <arg1> <arg2> <arg3> <arg4>

1st argument: is the defect key, which is unique for the defect
2nd argument: select which workflow to extract the data from, ex: ``screen``
3rd argument: select which charge, ex: -1
4th argument: select which spin, ex: 1.0
5th argument: select which state, ``ground`` (default) or ``excited``

The file is saved as: ``CONTCAR_defect_charge_spin_state.vasp``.
