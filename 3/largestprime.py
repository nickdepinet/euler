from itertools import chain, imap, ifilter
from time import time
"""
	Project Euler #3: Largest Prime Factor of 600851475143
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

@timeit
def solve(n):	
	return sorted(f for f in chain.from_iterable(imap(lambda r: (r, n / r), ifilter(lambda x: n % x == 0, xrange(1, int(n**0.5+1))))) if not any(ifilter(lambda y: f % y == 0, xrange(2, int(f**0.5+1)))))[-1]

print solve(600851475143)
