# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 22:12:53 2020

@author: rbv
"""

import numpy as np

def unique_elemts(x):
    """
    For a given array/list of (repeated) strings, this function creates an 
    array of the unique strings in the input array.
    
    Parameters:
    ----------
    x: (1-d) array-like 
       Contains strings.
    
    Returns:
    -------
    uni_x: (1-d) array-like 
           Contains unique string elements from input array. Note in non-trivial
           cases it will not have the same shape as x.
    """    
    

    # Creating empty list and appending unique string values
    uni_x = []
    for element in x:
        if element not in uni_x:
            uni_x.append(element)

    # Finally return a string array instead of a list
    return np.array(uni_x)


def days_number(month):
    """
    Returns the number of days for input month.
    
    Parameters:
    ----------
    month: str
           Month of interest.
   
    Returns:
    -------
    days: int
          Number of days corresponding to input month.
    
    """
    
    # Create a dictonary with the days of each month
    d = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "Nuvember": 30,
        "December": 31
    }

    # Assigining the value from the dictionary and return number of days
    days = d["{}".format(month)]
    return days


def sort_ind(x, y):
    """
    This function sorts the main array using np.argsort()
    and getting the indices, it sorts the dependent array.
    
    Parameters:
    ----------
    x: 1-D array to be sorted in ascending order.
    y: 1-D array that is dependent on x and will be sorted accordingly.
                
    Returns:
    -------
    sorted_x: 1-D sorted x array.
    sorted_y: 1-D sorted y array in accordance to x so any existing correlation is preserved. 
    """
    
    # Finding the sorted index array and applying it as a mask:
    idx = np.argsort(x)
    sorted_x, sorted_y = x[idx], y[idx]
    
    # Returning the sorted arrays
    return sorted_x, sorted_y


def filt_income(amount, category):
    """
    This function filters out the sources of income from an array containing
    monthly costs and their corresponding categories.
    
    Parameters:
    ----------
    amount: (1-d) array-like
            Contains the set of financial inputs read from a csv monthly file.
    category: (1-d) array-like
              contains the category corresponding to the amount array above. 
              Must have the same shape as amount array.
    
    Returns:
    -------
    costs: (1-d) array-like
           contains monthly costs where the income entries have been removed.
    cost_cats: (1-d) array-like
               contains corresponding category to monthly cost array. Has same
               shape as costs array
    """
    
    # Get rid of sources of income through array masking
    costs = amount[category != "Income"]
    cost_cats = category[category != "Income"]

    # Returning the income-masked arrays:
    return costs, cost_cats


def multi_costs(amount, category, days, month, income=False):
    """
    Calculates the cumulative costs for each category per day.
    
    Parameters:
    ----------
    amount: (1-d) array-like
            Contains the set of financial inputs read from a csv monthly file.
    category: (1-d) array-like
              contains the category corresponding to the amount array above. 
              Must have the same shape as amount array.
    days: (1-d) array-like
          log of day of the month when the each transaction was made. Must have
          the same shape as amount array.
    
    month: str
           month of instantiated class. Neccesary to extract number of days.
    income: (optional) boolean
            If set to True, calculates the cumulative sum of income entries
            for each day of the month
            
    Returns:
    -------
    multi_arr: (N-d) array-like
               contains the cumulative sum of costs/entries per day of the month.
               Shape is (n_cat x n_days).
    label_categ: (1-d) array-like 
                 contains sorted strings for each category.   
    """

    # Defining some general parameters
    n_days = days_number(month)

    day_arr = np.arange(1, n_days + 1)

    # Find the multi_cost for the actual costs (excluding income)
    if not income:
        # Filter out the income and sort array
        mask = (category != "Income")
        amount, category, days = amount[mask], category[mask], days[mask]
        idx = np.argsort(days)
        costs, costs_cats, days = amount[idx], category[idx], days[idx]
        
        #costs, costs_cats = sort_ind(*filt_income(amount, category))
        #days, costs_cats = sort_ind(*filt_income(days, category))
        
        label_categ = unique_elemts(costs_cats)
        n_cat = len(label_categ)

    if income:
        # Only extract income entries
        costs = amount[category == "Income"]
        costs_cats = category[category == "Income"]
        days = days[category == "Income"]

        # The number of categories will be just one i.e. income
        label_categ = np.array(["Income"])
        n_cat = 1

    # Now creating multi-dim array and appending cumulative values in a loop
    multi_arr = np.ones((n_cat, n_days))
    for i in range(n_cat):
        val = 0
        curr_cat = label_categ[i]
        for j in range(n_days):
            # Finding the cost of a particular day for the current category
            cost_day = np.sum(
                costs[(days == day_arr[j]) & (costs_cats == curr_cat)]) * -1
            # Note we are interested in the cumulative cost
            val += cost_day
            # Appending the cost to the multi-dim array
            multi_arr[i][j] = val
            
    # Returning the multi-dim array of cumulative costs with category array       
    return multi_arr, label_categ

#(days, amount, merchant, fees, category)

def mock_data(month, year, ntr_pd, curr):
    """
    Creates a csv file representing a mock bank statement. 
    This function is intended to create mock data to show data analysis assets
    to the public.
    
    Parameters:
    ----------
    
    
    Returns:
    -------
    
    """
    
    # First define # transactions per day and # days of the month
    n_days = days_number(month)
    
    # Declare number of categories (keep simple in this version of the function)
    categories = ["Groceries", "Drinks Out", "Coffee", 
                  "Eating Out", "Rent", "Others", "Income"]
    
    # Creating the main categories
    time_stamp = np.zeros(n_days)
    amount = np.zeros(n_days)
    category = np.zeros(n_days)
    
    # Defining fixed amounts
    rent = 3
    
    # Generating random data
    #for i in range(1, n_days+1):
        
        
    
    
    
    return None