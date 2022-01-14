# mortgage.py
#
# Exercise 1.7
"""
Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation. 
The interest rate is 5% and the monthly payment is $2684.11.
Here is a program that calculates the total amount that Dave will have to pay over the life of the mortgage:
"""
principal = 500000.0
rate = 0.05 #interest
payment = 2684.11 #monthly payment
total_paid = 0.0
months = 0

extra_payment_start_month = int(input("Which month will you start paying extra (expecting an integer)"))
extra_payment_end_month = int(input("Which month will you stop paying extra (expecting an integer)"))
extra_payment = int(input("How much will you pay extra"))

while principal > 0:
    if(extra_payment_start_month <= months < extra_payment_end_month):
        principal = principal * (1+rate/12) - (payment + extra_payment) 
        total_paid = total_paid + payment + extra_payment
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    
    months += 1
    print('Month', months, 'Total paid', total_paid, 'Principal remaining', principal)
    

