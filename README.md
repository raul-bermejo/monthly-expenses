# Monthly Expenses

## About

This repo is created as a project to track my transactions. Given a bank statement (in .csv format), this project is able to produce metrics and analytics of monthly transactions. 
At the time of writing, the code in monex.analytics.py produces three plots: 
1. Pie chart including the costs categories
2. (1x2) histogram with the costs and input transactions for each day of the month
3. Plot of the total costs and income over the month (expenses, income and net deficit/surplus)

## Dependencies & Installation

The code is written in Python and relies heavily on Pandas. For the code to produce visual analytics of monthly transactions, the following libraries are required: pandas, numpy and matplotlib. These can easily be installed using a package manager such as [pip](https://pip.pypa.io/en/stable/):

```bash
pip install numpy
pip install pandas
pip install matplotlib
```

Internally, the script monex.analytics.py uses a python script monex.utils.py in order to perform some computations and data transformations. In future versions of this software, the whole repo will be packaged in a library but for now the file monex.utils.py can be downloaded from the src folder.

# Functionality
To produce 

## Prospects

Below there is a list with the prospects I wish to achieve for this software tool:
- [x] Create "automated" metrics for personal monthly expense tracking
- [] Create a class to produce mock data
- [] Include a jupyter notebook to show the functionality of the software
- [] Train a model to recognise category by 
