balance = 1000
annualInterestRate = 0.05
balance_ = balance

monthly_interest_rate = annualInterestRate / 12.0
low = balance_ / 12
high = (balance * (1 + monthly_interest_rate) ** 12) / 12.0
epsilon = 0.01

while round(balance_, 2) != 0:
    balance_ = balance
    mid = (low + high) / 2.0

    for month in range(1, 13):
        monthly_interest_rate = (annualInterestRate / 12.0)
        monthly_unpaid_balance = balance_ - mid
        balance_ = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
        if balance_ <= 0:
            break
    
    balance_ = round(balance_, 2)
    
    if balance_ < epsilon and balance_ != 0:
        high = mid
    elif balance_ >= epsilon and balance_ != 0:
        low = mid
    else:
        break
    
print 'Lowest Payment:', round(mid, 2)
