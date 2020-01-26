n = 5
k = 3

rabbitsSeq = [0] * (n + 1)

rabbitsSeq[0] = 0
rabbitsSeq[1] = 1

for elm in range(2, len(rabbitsSeq)):
    rabbitsSeq[elm] = rabbitsSeq[elm - 1] + rabbitsSeq[elm - 2] * k

print('Result:', rabbitsSeq[-1])
