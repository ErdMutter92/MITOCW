import sys
def fib(x):
	global numCalls
	numCalls += 1
	assert type(x) == int and x >= 0
	if x == 0 or x == 1:
		return 1
	else:
		return fib(x-1) + fib(x-2)

if len(sys.argv) > 1:
	global numCalls
	numCalls = 0
	print fib(int(sys.argv[1]))
	print 'Number of time\'s fib was called: ', numCalls

'''
	the function fib calculates the fibminati
	given the position in th squence.
	Recersive Algorithum. 
'''
