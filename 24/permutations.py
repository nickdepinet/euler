from itertools import permutations

print list(map(''.join, permutations('0123456789')))[999999]
