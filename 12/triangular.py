from itertools import count, chain, imap
from time import time
"""
	Project Euler #12: what is the first triangle number of have over 500 divisors?
	Author: Nick Depinet
"""

def timeit(func):
	def timeitandrun(*args, **kwargs):
		start = time()
		results = func(*args, **kwargs)
		end = time()
		print ''.join(['took: ', str(end-start)])
		return results
	return timeitandrun

def factors(x):
	return list(chain.from_iterable(imap(lambda c: (c, x / c), filter(lambda i: x % i == 0, xrange(1, int(x**0.5+1))))))
def triangles():
	for x in count(1):
		yield sum(y for y in (xrange(0,x+1)))
@timeit
def solve():
	return next(x for x in triangles() if len(factors(x)) > 500)

print solve()
	
