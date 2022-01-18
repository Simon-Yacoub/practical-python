# pcost.py
#
# Exercise 1.27
import csv
'''
The columns in portfolio.csv correspond to the stock name,
 number of shares, and purchase price of a single stock holding. 
 Write a program called pcost.py that opens this file, 
 reads all lines, and calculates how much it cost
 to purchase all of the shares in the portfolio.
'''
#'Work/Data/portfolio.csv'
def portfolio_cost(filename):
    total_cost = 0
    try:
        f = open(filename)
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            total_cost = total_cost + int(row[1]) * float(row[2])
    except ValueError:
        print('Could\'nt parse line', row)
    return total_cost