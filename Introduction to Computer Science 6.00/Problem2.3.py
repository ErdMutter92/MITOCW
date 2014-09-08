#!/usr/bin/env python

## Using bisection search to figure out
## lowist possible mayment to pay off
## a credit card in a single year.

##Balance has an underscore to differentiate
## it from the testig balance value.
balance_ = 320000
interest = 0.2
epsilon = 0.01

## lowest possible payment needed per month,
## figuring if you did not have to pay any
## interest on the credit card/loan.
low = balance_ / 12.0

## highest possible payment needed per month,
## figuring if you did not make a payment until
## the vary last day after all interest is
## compounded monthly.
high = (balance_ * (1 + (interest / 12.0)) ** 12.0) / 12.0

while 1:
    ## Reset balance back to user input value
    balance = balance_
    ## the average of the highist and lowist possible payment.
    middle = (low + high) / 2.0
    
    interest_paid = 0
    
    for months in range(1, 13):
        interest_ = interest/12.0*balance
        interest_paid += interest_
        principal_paid = middle - interest_
        balance = balance - principal_paid
        
    if balance < epsilon:
        high = middle
    elif balance > epsilon:
        low = middle
    else:
        break
        
    print balance, round(middle, 2)