import math


def permutation(a, k=0):
    if k == len(a):
        print(' '.join(str(v) for v in a))
    else:
        for i in range(k, len(a)):
            a[k], a[i] = a[i], a[k]
            permutation(a, k + 1)
            a[k], a[i] = a[i], a[k]


n = 5
permut_list = list(range(1, n + 1))
print(math.floor(math.factorial(n) / math.factorial(n - n)))
permutation(permut_list)

