#!/bin/python

outstanding_balance = float(raw_input("What is the outstanding balance on the credit card: "))
annual_interest_rate = float(raw_input("What is the annual interest rate on the card: "))
min_monthly_payment_rate = float(raw_input("What is the minimum monthly payment rate on the card: "))

for i in range(1, 12):
    min_monthly_payment = round(min_monthly_payment_rate * outstanding_balance, 2)
    interest_paid = round(annual_interest_rate/12.0 * outstanding_balance, 2)
    principle_paid = round(min_monthly_payment - interest_paid, 2)
    outstanding_balance = round(outstanding_balance - principle_paid, 2)
    print "Month: ", i
    print "Minimum Monthly Payment: ", min_monthly_payment
    print "Principle Paid: ", principle_paid
    print "Remaining Balance: ", outstanding_balance