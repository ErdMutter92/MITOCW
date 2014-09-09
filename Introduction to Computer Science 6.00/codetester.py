balance = 9999999999999
annualInterestRate = 0.2
balance_ = balance

monthly_interest_rate = annualInterestRate / 12.0
low = balance / 12
high = (balance * (1 + monthly_interest_rate) ** 12) / 12.0
epsilon = 0.01
trys = 0

while round(balance_, 2) != 0:
    balance_ = balance
    mid = (low + high) / 2.0

    #print low,mid,high

    for month in range(1, 13):
        trys += 1
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
    
    #if str(high) == str(low) == str(mid):
    #    break
        
    
print 'Lowest Payment:', round(mid, 2)
print trys, balance_