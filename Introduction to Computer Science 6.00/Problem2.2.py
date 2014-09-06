#!/bin/python

## Paying Debt Off In a Year

outstanding_balance_save = float(raw_input("Enter the outstanding balance on your credit card: "))
interest_rate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))

print "RESULT"

count = 0
while 1:
    count = count + 1
    payment = 10 * count
    outstanding_balance = outstanding_balance_save
    for i in range(1, 13):
        ## Removed un-necisary bulk from the program.
        #interest_paid = round(interest_rate/12.0 * outstanding_balance, 2)
        #principle_paid = round(payment - interest_paid, 2)
        #outstanding_balance = round(outstanding_balance - principle_paid, 2)
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