# Carbon Emission Analysis
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/walkenho/carbon-emission-analysis/main?labpath=EmissionDataAnalysis.ipynb)
(Binder currently broken! Back soon!)

## Introduction

This project demonstrates some analysis of carbon emission data for ships. The data can be downloaded from the [EU-MRV system](https://mrv.emsa.europa.eu/#public/emission-report).

In this project I focus on the following four questions:

* How many ships of each type are included in the dataset?
* How do the emissions profiles differ for the different ship types?
* What is the relationship between ship deadweight and emissions intensity?
* How many miles did each vessel in the database travel?

Questions that I would like to explore in the future are:

* Which ships stopped being operated? Is there a correlation between a vessel's efficiency and if it is still being operated?
* This report details the guidelines for the EDI. It would be interesting to plot the current data set together with these values for the guidelines.
* The dataset at hand does not contain the build years of the ships. However, we can get these from https://www.vesselfinder.com. It would be interesting to plot the efficiency values against build years for different vessel types, in particular in combination with the emission guidelines.

## How to Use
### Using Poetry
#### Installation

Run `make install` to install the necessary software packages. 

#### Execution

Run `make presentation` to show the Jupypter Lab notebook.

### Without Poetry

* Option 1: Run on [Binder](https://mybinder.org/v2/gh/walkenho/carbon-emission-analysis/main?labpath=EmissionDataAnalysis.ipynb) (Currently broken :( Back soon!)
* Option 2: Install the necessary libraries and run wherever you like :)
