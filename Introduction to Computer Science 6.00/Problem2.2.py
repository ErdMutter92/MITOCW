outstanding_balance_ = float(raw_input('Balance: '))
interest_rate = float(raw_input('Rate: '))

count = 0
while 1:
    payment = 10 * count
    outstanding_balance = outstanding_balance_
    for month in range(1, 13):
        monthly_interest_rate = (interest_rate / 12.0)
        monthly_unpaid_balance = outstanding_balance - payment
        outstanding_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
        if outstanding_balance <= 0:
            break
    if outstanding_balance <= 0:
        break
    count += 1

print 'Lowest Payment:', payment