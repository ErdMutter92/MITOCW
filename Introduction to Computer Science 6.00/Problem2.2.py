#!/bin/python

## Paying Debt Off In a Year given a outstanding balance and interest rate.

outstanding_balance_save = float(raw_input("Enter the outstanding balance on your credit card: "))
interest_rate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))

print "RESULT"

count = 0
while 1:
    count = count + 1
    payment = 10 * count
    outstanding_balance = outstanding_balance_save
    for i in range(1, 13):
        monthly_interest_rate = interest_rate / 12.0
        outstanding_balance = outstanding_balance * (1 + monthly_interest_rate) - payment
        if outstanding_balance < 0:
            months = i
            break
    if outstanding_balance < 0:
        break

print "Monthly payment to pay of debt in 1 year: ", payment
print "Number of months needed: ", months
print "Balance: ", round(outstanding_balance, 2)