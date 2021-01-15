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

# Usage
The monex.analytics.py script inputs a bank statement (in .csv format) to produce all the transaction analytics. Note that the format of the bank statement at the time of writing corresponds to the bank I use ([Transferwise]{https://transferwise.com/}). However, as long as your bank digitally produces a csv file with the following columns: "Date", "Amount", "Merchant", "Total fees", the software should work fine (or you can change the labelling of the columns in monex.analytics.py). 

The software at its current version has some limitations. Mainly, one has to clasify in the .csv file each of the transactions in an extra column labelled "Category" to produce figures 1. & 2. (see About section). 

## Prospects

Below there is a list with the prospects I wish to achieve for this software tool:
- [x] Create semi-automated metrics for personal monthly expense tracking
- [ ] Create a class to produce mock data
- [ ] Include a jupyter notebook to show the functionality of the software
- [ ] Automate Category recognition
  - [ ] Train a model to recognise category by analyse commerce (at least in Wellington CBD)
- [ ] Design ways of reducing biases (such as ATM withdrawal)
- [ ] Modify software to produce analytics of any arbitrary timespan
- [ ] Package software so it can be downloaded and used more easily
- [ ] Developed GUI to make software more user-friendly

## Authors

At the time of writing, all software has been humbly developed by [me]{http://raulbermejo.mystrikingly.com/}.

## Contributions 

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
