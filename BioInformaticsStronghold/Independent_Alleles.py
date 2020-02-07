import math

K = 7
N = 30

population = 2 ** K

probability_AaBb = 0.25
probability_failure = 0.75
totalProbability = 0

# Binomial Distribution formula
for i in range(N, population + 1):
    probability = (math.factorial(population) / (math.factorial(i) * math.factorial(population - i))) * \
                  (probability_AaBb ** i) * (probability_failure ** (population - i))
    totalProbability += probability

print(totalProbability)
