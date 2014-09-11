def balanceCalculator(balance, annualInterestRate, monthlyPaymentRate, loopMonths = 12, debug = False):
	#
	# Balance (Float); Outstanding balance of card at start.
	# annualInterestRate (Float); Annual Interest Rate defined by your bank/card.
	# monthlyPaymentRate (Float); Monthly Payment Rate defined by your bank/card (usually 0.02 or 0.04)
	# months (int); Number of months you wish to have the program calculate out
	# debug (bool); Print debug statements (Default: False)
	#
	# Returns (Tuple); [[min_monthly_payment, outstanding_balance], ..., [total_paid, outstanding_balance]]
	#

	outstanding_balance = float(balance)
	annual_interest_rate = float(annualInterestRate)
	min_monthly_payment_rate = float(monthlyPaymentRate)

	total_paid = 0
	returnList = []

	for i in range(1, loopMonths+1):
		innerTmpList = []
		monthly_interest_rate = annual_interest_rate / 12.0
		min_monthly_payment = min_monthly_payment_rate * outstanding_balance
		total_paid += min_monthly_payment
		monthly_unpaid_balance = outstanding_balance - min_monthly_payment
		outstanding_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)

		innerTmpList.append(round(min_monthly_payment, 2))
		innerTmpList.append(round(outstanding_balance, 2))	
	    
		if debug == True:
			print 'Month:', i    
			print 'Minimum monthly payment:', round(min_monthly_payment, 2)
			print 'Remaining balance', round(outstanding_balance, 2)

		returnList.append(innerTmpList)

	tmpList = []
	tmpList.append(round(total_paid, 2))
	tmpList.append(round(outstanding_balance, 2))
	returnList.append(tmpList)
	if debug == True:
		print 'Total paid:', round(total_paid, 2)
		print 'Remaining balance:', round(outstanding_balance, 2)

	return returnList

print balanceCalculator(1000, .03, .02)
