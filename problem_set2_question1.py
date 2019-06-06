# Problem Set 2, Question 1
"""
Calculates the credit card balance after one year if a person only pays the 
minimum monthly payment required by the credit card company each month.

The following inputs contain values as described below:
balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal

Returns remaining balance based on inputs. 
"""

def balance_one_year(balance, interest_rate, monthly_min):
    interest = interest_rate / 12
    for i in range(12):
        balance -= monthly_min*balance 
        balance += interest*balance
        answer = "Remaining balance: $" + str(round(balance, 2))
    return answer

balance_one_year(42, 0.2, 0.04)
