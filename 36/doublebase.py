"""
    Project Euler 36: Find the sum of all integers less than 1,000,000 which are palindromes in both base 10 and base 2
    Author: Nick Depinet
"""
print sum([x for x in range(0,1000000) if str(x) == str(x)[::-1] and str(bin(x))[2:] == str(bin(x))[2:][::-1]])
