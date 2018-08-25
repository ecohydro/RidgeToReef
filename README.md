# RidgeToReef

Jupyter notebooks for a binder-based module as part of the the Ridge to Reef program, August 2018

Authors: Kelly Caylor (caylor@ucsb.edu) and Natasha Krell (nkrell@ucsb.edu)

## Getting Started

To get started with the excercise, click here: [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/ecohydro/RidgeToReef/master?filepath=index.ipynb)


## About this Repo

This repository is a set of jupyter notebooks, data, and accompanying configuration files designed to be used with the [binder](mybinder.org) system. Through Binder, these notebooks provide an executable environment, making the code immediately reproducible by anyone, anywhere.

The following information is for authors of the module or others who wish to fork this repo and/or use it as the basis of their own efforts (but please see the Acknowledgements and Disclaimer below). 

**Students or anyone else wishing to simply _access_ the module can stop reading now and just use the [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/ecohydro/RidgeToReef/master?filepath=index.ipynb) link to start the module in their browser.**


Our analyses are built on the [Anaconda](https://www.anaconda.com/distribution/) python distribution, using [Python v.3.6](https://www.python.org/downloads/release/python-360/). 

### binder/

Configuration files are stored in the `binder/` folder of this repository. The `environment.yml` file contains required python packages. Note **this file cannot be auto-generated by `conda env export`.** You must instead specify the main requirements (e.g. `numpy`, `pandas`) and their versions. 

### data/

The `data/` folder contains all the necessary data files that are used in this excercise. These data were collected as part of the NSF projects acknowledged below, and **any use of these data outside of this excercise requires permission of the authors** (cf. contact information above).

### assets/

Any images, files, or other resources used in the notebooks are contained in the `assets/` folder. 

# Acknowledgements & Disclaimer

This material is based upon work supported by the National Science Foundation under Grants No. [SES-1534544](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1534544&HistoricalAwards=false) and [SES-1360421](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1360421&HistoricalAwards=false). Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.
