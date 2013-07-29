from math import factorial
"""
	Project Euler #20: Find the sum of the digits of 100!
"""

print sum(int(c) for c in str(factorial(100)))
