"""
    Project Euler Problem #4: Largest palindrome product of two 3-digit integers
    Author: Nick Depinet
"""

print sorted([x*y for x in range(100,1000) for y in range(100,1000) if str(x*y) == str(x*y)[::-1]])[-1]

