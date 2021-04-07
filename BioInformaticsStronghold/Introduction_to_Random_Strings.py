from math import log10

dna = 'TGGTGTTGTGAGATGCTTTGCATCGAGCTAATAGTACTAATACAAGCGAGAAGCTGACGATACAAAATGTTTGGGACTCCGGACCC'
probabilities = '0.075 0.153 0.223 0.262 0.299 0.402 0.416 0.502 0.573 0.619 0.661 0.756 0.771 0.872 0.911'

GC = dna.count('C') + dna.count('G')
TA = dna.count('T') + dna.count('A')

prop = probabilities.split()
res = ["{:.3f}".format(log10((((1 - float(p)) / 2) ** TA) * (float(p) / 2) ** GC)) for p in prop]

print(' '.join(res))