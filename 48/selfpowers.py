"""
	Project Euler #48: Find the last ten digits of the series:
	1^1+2^2+3^3+...+1000^1000
	Author: Nick Depinet
"""

print str(sum(d**d for d in xrange(1,1001)))[-10:]
