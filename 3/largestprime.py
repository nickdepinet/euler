from itertools import chain, imap, ifilter
import collections
"""
	Project Euler #3: Largest Prime Factor of 600851475143
	Author: Nick Depinet
"""

print collections.deque(sorted(f for f in chain.from_iterable(imap(lambda r: (r, 600851475143 / r), ifilter(lambda x: 600851475143 % x == 0, xrange(1, 600851475143**0.5+1)))) if not any(ifilter(lambda y: f % y == 0, xrange(2, f**0.5+1)))))
