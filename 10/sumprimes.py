from itertools import ifilter
"""
	Project Euler #10: Find the sum of all primes below 2 million
	Author: Nick Depinet
"""

print sum(p for p in xrange(3, 2000000, 2) if not any(ifilter(lambda f: p % f == 0, xrange(2, int(p**0.5+1)))))+2
