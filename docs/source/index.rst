ADAQ: Automatic Defect Analysis and Qualification
===================================

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Getting Started

   installation
   overview
   tutorial

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Workflows

   General
   0_chemical_potential
   1_unitcell
   2_node_scaling
   3_host_supercell
   4_screen

.. figure:: ADAQ_logo_header.png
  :scale: 30%
  :align: left
  :target: index.html

**ADAQ** is a collection of automatic workflows used for high-throughput calculations of point defects in semiconductors.
These workflows are implemented using the High-Throughput Toolkit (|httk|_).

|httk|_

.. _httk: https://github.com/httk/httk

.. |_httk| replace:: *httk*

Required software
------------

* Python 2.7
* |tess|_ (https://github.com/wackywendell/tess)
* |PyVaspwfc|_ (embedded)
* |httk|_
* isotropy
* jmol (optional)

.. _tess: https://github.com/wackywendell/tess

.. _PyVaspwfc: https://github.com/QijingZheng/VaspBandUnfolding/blob/master/vaspwfc.py


How to Cite
------------

The preferred citation for ADAQ:

.. code-block::

   @article{ADAQ,
   title = {ADAQ: Automatic workflows for magneto-optical properties of point defects in semiconductors},
   journal = {Computer Physics Communications},
   volume = {269},
   pages = {108091},
   year = {2021},
   issn = {0010-4655},
   doi = {https://doi.org/10.1016/j.cpc.2021.108091},
   url = {https://www.sciencedirect.com/science/article/pii/S0010465521002034},
   author = {Joel Davidsson and Viktor Ivády and Rickard Armiento and Igor A. Abrikosov},
   keywords = {Point defects, Semiconductors, Density functional theory, Photoluminescence, Automatic workflow, Python}
   }

.. note::

   This project is under active development.

