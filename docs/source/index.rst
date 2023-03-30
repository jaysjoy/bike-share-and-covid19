.. bikeshare documentation master file, created by
   sphinx-quickstart on Tue Mar 28 17:57:41 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Dynamics of trip clusters amid the pandemic 
===========================================

Update: 2023/03/30 

 * Implemented clustering models to bikeshare trips during different stages of the covid 19 outbreak.
 * Each covid period was calibrated with a clustering pipeline. The pipeline includes a component of factor analysis of mixed data (FAMA), standardization, and a DBSCAN clustering module. 
 * FAMA is a principal component analysis technique that works well both a mixture of numerial and categorical data. Original high dimensional data was reduced to a lower dimensional space. 
 * DBSCAN is a clustering algorithm that identifies clusters via the distance among data points. Hence, it is better to keep the dimension of input data relatively small, and this is why FAMA was introduced before applying DBSCAN. For more information on the technicalities, plese refer to :ref:`methods <methods>`.
 * Generating other stats resulting from the cluster modeling (*ongoing*). 

The following are slides that keep updating. The lastest slides go first. 

.. toctree::
   :maxdepth: 2
   :caption: Slides:
   
   progress/prepancluster
   progress/precbcluster
   progress/cbcluster
   progress/postcbcluster

.. toctree:: 
   :maxdepth: 2
   :caption: Approach:

   Approach/method


.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
