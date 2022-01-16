# pcost.py
#
# Exercise 1.27
'''
The columns in portfolio.csv correspond to the stock name,
 number of shares, and purchase price of a single stock holding. 
 Write a program called pcost.py that opens this file, 
 reads all lines, and calculates how much it cost
 to purchase all of the shares in the portfolio.
'''
total_cost = 0
with open('Work/Data/portfolio.csv', 'rt') as f:
    next(f)
    for line in f:
        row = line.split(',')
        total_cost = total_cost + int(row[1]) * float(row[2])
    
    print('Total cost', total_cost)