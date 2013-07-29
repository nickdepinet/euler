from itertools import count
"""
	Project Euler #12: what is the first triangle number of have over 500 divisors?
	Author: Nick Depinet
"""

def numFactors(x):
	return len(filter(lambda i: x % i == 0, xrange(1, x/2+1)))+1
def triangles():
	for x in count(1):
		yield sum(y for y in (xrange(0,x+1)))

print next(x for x in triangles() if numFactors(x) > 500)
