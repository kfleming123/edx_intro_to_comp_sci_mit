# Problem Set 2, Question 2
"""
Calculates the minimum fixed monthly payment needed in order pay off a credit 
card balance within 12 months. 

The following inputs contain values as described below:

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal

Returns the lowest monthly payment that will pay off all debt in under 1 year.
"""
def min_monthly_bisection(balance, annualInterestRate):
    interest = annualInterestRate / 12
    remainder = 1
    lower_bound = balance / 12
    upper_bound = (balance * (1 + interest)**12 / 12)
    while remainder > 0:
        guess = (lower_bound + upper_bound) / 2
        test_balance = balance
        for i in range(12):
            test_balance -= guess
            test_balance += interest*test_balance
        if round(test_balance, 2) == 0:
            break
        elif round(test_balance, 2) > 0:
            lower_bound = guess
        else:
            upper_bound = guess
    return("Lowest Payment: {:.2f}".format(guess))

min_monthly_bisection(500, 0.15)