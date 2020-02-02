import numpy as np

population = np.array([1.0, 0.0, 0.0, 1.0, 0.0, 1.0])

probabilities = np.array([1.0, 1.0, 1.0, 0.75, 0.5, 0.0])

offspring = sum(2 * population * probabilities)

print(offspring)
