import itertools

samples = []
n = 5

for i in itertools.permutations(list(range(1, n + 1))):
    for j in itertools.product([-1, 1], repeat=len(list(range(1, n + 1)))):
        perm = [a * sign for a, sign in zip(i, j)]
        samples.append(' '.join(str(v) for v in perm))

print(len(samples))
for i in samples:
    print(i)