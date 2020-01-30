n = 92
m = 18

rabbitsSeq = [0] * (n + 1)

rabbitsSeq[0] = 0
rabbitsSeq[1] = 1

for elm in range(2, len(rabbitsSeq)):
    if elm <= m:
        rabbitsSeq[elm] = rabbitsSeq[elm - 1] + rabbitsSeq[elm - 2]
    elif elm == (m+1):
        rabbitsSeq[elm] = rabbitsSeq[elm - 1] + rabbitsSeq[elm - 2] - 1
    elif elm > m:
        rabbitsSeq[elm] = rabbitsSeq[elm - 1] + rabbitsSeq[elm - 2] - rabbitsSeq[elm - (m+1)]

print(rabbitsSeq[-1])
