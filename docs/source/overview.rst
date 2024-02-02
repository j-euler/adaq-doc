============
Overview
============

ADAQ automates the following steps in the theoretical process of calculating point defects:

* relaxes the host unit cell.
* creates the defect supercells with arbitrarily sized defect clusters.
* screens these defects for the most relevant properties.
* fully characterizes the point defects including zero phonon lines (ZPL), zero field splitting (ZFS), and hyperfine coupling parameters.

..
   For more information: <https://httk.org/adaq/>

This overview introduces the ADAQ commands and folder structure..
More details are found in :doc:`tutorial`.

Ensure to source *httk* and ADAQ as well as activate the conda enviroment:

.. code-block:: console

   $ source /path/to/httk/init.shell
   $ source /path/to/ADAQ/init.shell
   $ conda activate adaq

.. _commands:

ADAQ commands
=============

The ADAQ commands are available after sourcing ADAQ/init.shell.
They all start with ``adaq-``.
More details are found in :doc:`commands`.

.. _project:

ADAQ project
=============

Here is how a ADAQ project is created.
Navigate to where you would like to store the ADAQ project.
Run the following ADAQ command:

.. code-block:: console

   $ adaq-set-up-project <name>

Where ``<name>`` refers to the host material.

You will then be prompted to provide a ``POSCAR`` for the unit cell.
It does not need to be relaxed, there are ADAQ workflows to do that.

..
   More details about the workflows are here :doc:`tutorial`.
   interface with mp-ids?

One also needs to provide additional parameters that are not calculated.
These are:
* Dielectric constant
* refractive index

.. todo::

   There will also be some metadata to add, such as project, and collaborators etc.

The command will also set up a httk project.
You will be prompted to set up a public key that identifies you as the owner, which is recommended.

.. _folder:

ADAQ folder
===========

After the ``adaq-set-up-project`` command has finished.
You will now have a folder titled ``<name>`` with subfolders for the different workflows.
It will also contain:

* ``<name>``.vasp that is the POSCAR of the unit cell.
* ``<name>``.data that contain the dielectric constant and refractive index.
* parameters.py that have the settings for the defect generation.
* ht.project that has the settings for the defect generation.

You will also need to set up a supercomputer with the httk command:
.. code-block:: console

   $ httk-computer-setup

Follow the prompt to set up a new computer.
This will add a computer to the computers folder inside the ht.project.
There is also a ``config`` file that you can edit in case you need to change something.

Depending on your supercomputer cluster, you may need to edit the ht.project/computers/<computer name>/start-taskmgr to load module or python environments during the runs.

To install httk at the remote computer, run the following command:
.. code-block:: console

   $ httk-computer-install <computer name>

Go to :doc:`tutorial` to calculate the single defects in 4H-SiC using ADAQ.

Linköping University specifics
------------------------------

Here are the following settings to set up a computer for tetralith:

* Add a project computer
* Use the ssh-slurm templete
* Name: tetralith
* Remote Hostname: tetralith.nsc.liu.se
* Username: x_abcde
* Directory on remote host: /proj/theophys/users/x_abcde/httk (Important keep as short as possible)
* Command to run vasp: mpprun /software/sse/manual/vasp/5.4.4.16052018/nsc2/vasp_gam
* VASP pseudopotential path: /software/sse/manual/vasp/POTCARs/PBE/2015-09-21/
* Slurm project to submit jobs to: naissYYYY-X-Z
* Slurm job timeout: 168:00:00 (max walltime at tetralith)
* Taskmanager timeout max time per task in seconds: 604800 (max walltime in seconds)

When using dedur and tetralith, also change these:

In ht.project/computers/name/pull, change: -az to -rltz

In ht.project/computers/name/start-taskmgr, add:
.. code-block:: console

   $ module load Anaconda/2023.09-0-hpc1
   $ conda activate adaq2

after source "\$HTTK_DIR/setup.shell" 

.. _database:

ADAQ database
=============

Once a project is finished, the data can be added to the ADAQ database.
Go to :doc:`database` for more information.


