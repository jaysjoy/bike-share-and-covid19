% bikeshare documentation master file, created by
% sphinx-quickstart on Tue Mar 28 17:57:41 2023.
% You can adapt this file completely to your liking, but it should at least
% contain the root `toctree` directive.

# Dynamics of trip clusters amid the pandemic

```{include} ../../README.md
```
```{rubric} the new looking theme of furo. 
```
in line math $x=\sum \frac{2}{3}^2$.


$$
x = 2 * \frac{3}{4}
$$ (eqn:exg)

```{warning}
This project is under heavy development. 
```
{ref}`Overall framework` provides a good overview of the modeling roadmap. 

```python
# testing block 
```
> another quote     


```{code-block} python
x_str = "testing this new function"
# jump to another section
```
```{tip}
Please follow along online resources to beautify styling. 
```

> quote; new theme looks nice 

## Latest updates 

Concise update and general intro: 2023/03/30

> - Implemented clustering models to bikeshare trips during different stages of the covid 19 outbreak.
> - Each covid period was calibrated with a clustering pipeline. The pipeline includes a component of factor analysis of mixed data (FAMA), standardization, and a DBSCAN clustering module.
> - FAMA is a principal component analysis technique that works well both a mixture of numerial and categorical data. Original high dimensional data was reduced to a lower dimensional space.
> - DBSCAN is a clustering algorithm that identifies clusters via the distance among data points. Hence, it is better to keep the dimension of input data relatively small, and this is why FAMA was introduced before applying DBSCAN. For more information on the technicalities, please check with {doc}`Approach/method`. To start with, please read {ref}`Overall framework`. 
> - Generating other stats resulting from the cluster modeling (*ongoing*).

The following are slides that keep updating. The lastest slides go first.

```{toctree}
:caption: Slides
:maxdepth: 2

progress/tasks
progress/prepancluster
progress/precbcluster
progress/cbcluster
progress/postcbcluster
```

```{toctree}
:caption: 'Approach:'
:maxdepth: 2

Approach/method
```

% Indices and tables

% ==================

% * :ref:`genindex`

% * :ref:`modindex`

% * :ref:`search`
