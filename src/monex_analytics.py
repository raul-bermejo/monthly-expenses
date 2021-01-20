# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 21:23:38 2020

@author: rbv

INPUT: A csv file with all the transactions from transferwise (or a compatible
csv bank statement, see README)

Each transaction (paid money or others) will be put in different categories:
    (a) Groceries
    (b) Eating out
    (c) Coffee
    (d) Rent
    (e) Medical stuff
    ...
    
OUTPUT: Analytics of the costs, including:
    (a) Pie chart including the costs categories
    (b) 1x2 histogram with the costs and input transactions for each day
    (c) Plot of the costs over time (where each line is a cost)
    (d) Plot of money that went into fees
"""

# Importing all neccesary modules and plot settings
#%config InlineBackend.figure_format = 'retina'   # to see plots in HD
import random as ra
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from monex_utils import *
from jupyterthemes import jtplot
jtplot.style(theme='monokai', context='notebook', ticks=True, grid=False)

plt.rc('axes', titlesize=20)  # fontsize of the axes title
plt.rc('axes', labelsize=20)  # fontsize of the x and y labels
plt.rc('xtick', labelsize=20)  # fontsize of the tick labels
plt.rc('ytick', labelsize=20)  # fontsize of the tick labels
plt.rc('legend', fontsize=18)  # legend fontsize
plt.rc('figure', titlesize=20)  # fontsize of the figure title
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

PATH_TO_FOLDER = r"C:\Users\rbv\OneDrive\Escritorio\Side__Projects\Monthly_Expenses\my-expenses"

class MonthlyExpenses_Dataset:
    "Document class later"
    
    def __init__(self, month, year):
        """
        Constructor of MonthlyExpenses_Dataset.
        
        Parameters:
        ----------

        month: int
               Number of the month of mocked data
        year: int
              Year of mocked data
        
        """
        
        self.month = month
        self.year = year
    
    def crceate_mock_data(random_set=False):
    """
    Creates a pandas.DataFrame representing a mock bank statement. 
    
    Parameters:
    ----------
    random_set: bool
                If True, all data is set random by default. Otherwise, some of the overall costs are set randomly 
    
    Returns:
    -------
    
    Notes:
    -----
    This function is intended to create mock data to show data analysis assets
    to the public.
    """
    
    # Initialize some data
    categories = ["Groceries", "Drinks Out", "Coffee", 
                      "Eating Out", "Rent", "Others", "Income"]
    
    if random_set is not True:
        month = month_name(np.random.randint(1,12))
        year = np.random.randint(2019,2021)
        
        # Define some (arbitrary) average weekly expenses
        AVERAGE_RENT = 260
        AVERAGE_GROCERIES = 100
        AVERAGE_EATING_OUT = 50
        AVERAGE_DRINKING_OUT = 30
        AVERAGE_COFFEE = 30
        AVERAGE_OTHERS = 20
        AVERAGE_INCOME = 1000
        
        
        # Define fixed weekly payments
        rent = np.random.normal(AVERAGE_RENT, scale=AVERAGE_RENT//10)
        groceries = np.random.normal(AVERAGE_GROCERIES, scale=AVERAGE_GROCERIES//10)
        income = np.random.normal(AVERAGE_INCOME, scale=AVERAGE_INCOME//100)
        
        # Define sporadic expenses
    

        # Declare number of categories (keep simple in this version of the function)
        

        # Creating the main categories
        time_stamp = np.zeros(n_days)
        amount = np.zeros(n_days)
        category = np.zeros(n_days)

        # Defining fixed amounts
        rent = 3
    
    # Generating random data
    #for i in range(1, n_days+1):

class MonthlyExpenses_Analytics:

    def __init__(self, month):
        """
        Initiaties class by inputting the month to perform the data analysis of
        costs.
        """
        self.month = month
        self.PATH_TO_FOLDER = PATH_TO_FOLDER

    def data_extract(self, print_time=False, df_display=False):
        """
        Reads csv bank statement from instantiated month and extracts relevant
        data into arrays.
        
        Parameters:
        ----------
        print_time: (optional) boolean
                    Gives the user the option to print how much time it takes
                    to load bank statement data. Set to False by default.
        df_display: (optional) boolean
                    Displays the first entries of csv bank statement. By default
                    it is set to False.
                    
        Returns:
        -------
        days: (1-d) array-like
              contains the set of day of the month when each transaction was made.
        amount: (1-d) array-like
                contains the magnitude (amount) of each transaction.
        merchant: (1-d) array-like
                  contains the soruce of each transaction (e.g. commerce,
                  company, etc...). Entries will be empty if card could not track
                  source.
        fees: (1-d) array-like
              conains the fees that the bank charged for each transaction.
        category: (1-d) array-like
                  contains the set of strings with the corresponding category 
                  for each transaction.  
        """
        
        # Loading the file with pandas
        loc = self.PATH_TO_FOLDER + "\{}.csv".format(self.month)
        
        start = time.time()
        df = pd.read_csv(loc,sep=',',
                         usecols=["Date", "Amount", "Merchant", "Total fees", "Category"])
        timestamp, amount, merchant, fees, category = df.values.T
        end = time.time()

        if print_time:
            print("The Bankstatement csv file took {:.3f} s to load.".format(
                end - start))
            
        if df_display:
            pd.display(df)

        # Now turning the timestamp into a day array
        timestamp, amount, merchant, fees, category = df.values.T
        days = pd.to_datetime(timestamp, dayfirst=True).day.values
        # Return the extracted arrays
        return days, amount, merchant, fees, category

    # Now creating a set of methods to display each of the required listed graphics above:

    def pie_chart(self, savefig=False):
        """
        Produces and displays pie-chart indicating the percetange of the total monthly cost
        spent in each category.
        
        Parameters:
        ----------
        savefig: (optional) boolean
                 saves displayed pie-chart in current directory.
                 
        Returns:
        -------
        None: pie-chart is produced but axis are not returned.
        
        """

        # First extract the data to be used i.e. category and amount
        days, amount, merchant, fees, category = self.data_extract(
            print_time=True)
        
        start1 = time.time()
        # Setting the labels, colors and explode for piechart:
        labels = np.sort(unique_elemts(category[category != "Income"]))
        n_cat = len(labels)
        color = colors[8:n_cat+9]

        # Now , we need to mask the income and sort the categories and costs via index sorting
        costs, pie_cat = sort_ind(*filt_income(amount, category))

        # Finding total costs and percentage spent in each category
        total = np.sum(costs)
        perc_costs = np.zeros(n_cat)
        for i in range(n_cat):
            perc_costs[i] = np.sum(costs[pie_cat == labels[i]]) / total * 100

        perc_costs = np.abs(perc_costs)
        # Creating explode so some categories are highlighted
        explode = np.zeros(n_cat)
        explode[labels == 'Drinks Out'] = 0.15
        explode[labels == 'Eating Out'] = 0.15
        explode[labels == 'Groceries'] = 0.15

        # Creating the piechart
        plt.figure(figsize=(13, 9))
        pie = plt.pie(perc_costs,
                      colors=colors[7:],
                      explode=explode,
                      shadow=True,
                      startangle=0)

        # Creating independent legend with labels so text nor percentage overlaps
        plt.gca().axis("equal")
        new_label = [
            "{} - {:.1f}%".format(labels[i], perc_costs[i])
            for i in range(len(labels))
        ]
        plt.legend(pie[0],
                   new_label,
                   bbox_to_anchor=(0.75, 0.85),
                   loc=0,
                   bbox_transform=plt.gcf().transFigure)

        plt.title("Expenses of {} per category: Total of {:.2f} NZD".format(
            self.month, -1 * total))
        plt.tight_layout()
        if savefig:
            plt.savefig("Expenses__PieChart__{}.png".format(self.month),
                        format='png',
                        dpi=200,
                        pad_inches=0.1,
                        bbox_inches='tight')
        plt.show()
        end1 = time.time()
        print("The data processing and pie-chart plotting took {:.2f} s".format(end1-start1))

    def cost_plot(self, savefig=False):
        """String-doc method later"""

        # Extracting the data
        days, amount, merchant, fees, category = self.data_extract()
        
        start1 = time.time()
        # We need to crate a multidimensional array (n_cat x n_days) s.t. it contains the cumulative amount of costs per category
        costs, cost_labels = multi_costs(amount, category, days, self.month)
        daily_costs = costs.T
        total_costs = [np.sum(daily_costs[i]) for i in range(np.shape(daily_costs)[0])] 

        # Finding the income values and total cumulative costs
        income, dummy_label = multi_costs(amount,category,days,self.month,income=True)
        
        # Creating an array with the number of days in the week
        n_days = days_number(self.month)
        day_arr = np.arange(1, n_days + 1)

        # Displaying the costs, income and fees as a function of time
        fig, ax = plt.subplots(2, 1, figsize=(9, 14), sharex=True)
        ax = ax.flatten()
        
        # Plotting specific costs 
        for i in range(len(cost_labels)):
            ax[0].plot(day_arr, costs[i], label=cost_labels[i], color=colors[i+7])
        
        # Plotting overall costs and incomes
        ax[1].plot(day_arr, income[0] * -1, 
                   label="Income: NZD{:.2f}".format(income[0][-1] * -1), color=colors[0])
        ax[1].plot(day_arr, total_costs, 
                   label="Total Costs: NZD{:.2f}".format(total_costs[-1]), color=colors[2])
        ax[1].plot(day_arr, (income[0] * -1) - total_costs, 
                   label="Savings: NZD{:.2f}".format(((income[0] * -1) - total_costs)[-1]),color=colors[1])
        
        
        for i in range(2):
            ax[i].grid(True)
            ax[i].legend(loc=0)
            ax[i].set_ylabel('Amount [NZD]')

        # Setting up aesthetical features
        ax[1].set_xlabel('Day of the month')
        ax[0].set_title("Detailed costs of {} as a function of time".format(self.month))
        #ax[1].set_title("Income of {} as a function of time".format(self.month))
        plt.tight_layout()
        
        if savefig:
            plt.savefig("Expenses__Plot__{}.png".format(self.month),
                format='png',
                dpi=200,
                pad_inches=0.1,
                bbox_inches='tight')
        
        plt.show()
        end1 = time.time()
        print("The data processing and detailed cost plotting took {:.2f} s".format(end1-start1))

        
    def histogram(self, savefig=False):
        """
        Extracts csv data of balances and creates a histogram of the number of
        transactions per day and number of transactions per category.
        
        Parameters:
        ----------
        savefig: (optional) boolean
                 saves the set of histograms in current directory.
                 
        Returns:
        -------
        None: It plots the histgrams without returning axes.
        """

        # Extracting the data
        days, amount, merchant, fees, category = self.data_extract()
        
        start1 = time.time()
        # We want to create two histograms: one tracking the amount of transactions
        # per day of the month and the amount of transactions per category
        fig, ax = plt.subplots(1, 2, figsize=(16, 9), sharey=True)
        ax = ax.flatten()

        ax[0].hist(days, bins=days_number(self.month))
        ax[1].hist(category, bins=len(unique_elemts(category)))

        ax[0].set_ylabel("Counts")
        ax[0].set_xlabel("Days")
        ax[0].set_title("# of transactions per day of the month")

        ax[1].set_title("# of transactions per category")
        # Tilting x-labels so they don't overlap
        ax[1].set_xticklabels(unique_elemts(category), rotation=60)
        plt.tight_layout()
        
        # Giving the option to save the figure:
        if savefig:
            plt.savefig("Expenses__Histogram__{}.png".format(self.month),
                        format='png',
                        dpi=200,
                        pad_inches=0.1,
                        bbox_inches='tight')
        plt.show()
        end1 = time.time()
        print("The data processing and histogram displaying took {:.2f} s".format(end1-start1))

    """
       TO DO:
           (1) Debug multi_arr function so July finances are consistent.
           (3.5) Included small plot of fees for cost_plot() method & wrapped legend
           (a) Created function to generate csv mock Bank statement (Use Gaussian in all cases!!)
               (i) For fees, generate the via a Gaussian centered around 0
               (iv) For drinks
               (iii) For rent, create something consistent
           (!) Sent message to Felix and arranged a meeting
           (5) Migrated functions to other module to import from current code
           
        IDEAS FOR FUTURE VERSIONS:
            (!) Make class robust for different banks (i.e. so it does not only work with Transferwise)
            (a) Make the number of categories customizable for each program/instantiation
            (b) Use AI (PyTorch) to identify merchant and put in given category (?) - Long term idea
            (c) Create GUI to display improve layman's user experience (?) - Long term idea
    """

