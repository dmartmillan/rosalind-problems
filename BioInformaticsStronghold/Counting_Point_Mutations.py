dna_1 = "GAGCCTACTAACGGGAT"
dna_2 = "CATCGTAATGACGGCCT"

mutations = 0

for i in range(0, len(dna_1)):
    if dna_1[i] != dna_2[i]:
        mutations += 1

print(mutations)