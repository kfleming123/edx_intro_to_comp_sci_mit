# Problem Set 2, Question 2
"""
Calculates the minimum fixed monthly payment needed in order pay off a credit 
card balance within 12 months. 

The following inputs contain values as described below:

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal

Returns the lowest monthly payment (in increments of $10) that will pay off 
all debt in under 1 year.
"""

def min_monthly(balance, annualInterestRate):
    interest = annualInterestRate / 12
    guess = 10
    remainder = 1
    while remainder > 0:
        test_balance = balance
        for i in range(12):
            test_balance -= guess
            test_balance += interest*test_balance
        if test_balance <= 0:
            break
        guess +=10
    return("Lowest Payment: {:.2f}".format(guess))

min_monthly(500, 0.15)