from math import factorial, floor

n = 95
r = 9

P = (factorial(n) / factorial(n - r)) % 1000000

print(floor(P))
