k = 23
m = 23
n = 30

organisms = k + m + n

probability = (4 * (k * (k - 1) + 2 * k * m + 2 * k * n + m * n) + 3 * m * (m - 1)) / (4 * organisms * (organisms - 1))

print(probability)
