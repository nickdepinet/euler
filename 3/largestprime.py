from itertools import chain, imap, ifilter
import collections
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
def solve():	
	return collections.deque(sorted(f for f in chain.from_iterable(imap(lambda r: (r, 600851475143 / r), ifilter(lambda x: 600851475143 % x == 0, xrange(1, int(600851475143**0.5+1))))) if not any(ifilter(lambda y: f % y == 0, xrange(2, int(f**0.5+1))))), maxlen=1)

print solve()
