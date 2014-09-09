#!/bin/python

outstanding_balance = float(raw_input("What is the outstanding balance on the credit card: "))
annual_interest_rate = float(raw_input("What is the annual interest rate on the card: "))
min_monthly_payment_rate = float(raw_input("What is the minimum monthly payment rate on the card: "))

total_paid = 0

for i in range(1, 13):
    monthly_interest_rate = annual_interest_rate / 12.0
    min_monthly_payment = min_monthly_payment_rate * outstanding_balance
    total_paid += min_monthly_payment
    monthly_unpaid_balance = outstanding_balance - min_monthly_payment
    outstanding_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
    print 'Month:', i
    print 'Minimum monthly payment:', round(min_monthly_payment, 2)
    print 'Remaining balance', round(outstanding_balance, 2)

print 'Total paid:', round(total_paid, 2)
print 'Remaining balance:', round(outstanding_balance, 2)