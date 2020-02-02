from Bio import SeqIO

seq_DNA = []

for seq_record in SeqIO.parse("rosalind_lcsm.txt", "fasta"):
    seq_DNA.append(str(seq_record.seq))

seq_DNA_Sorted = sorted(seq_DNA, key=len)

first = seq_DNA_Sorted[0]
compare = seq_DNA_Sorted[1:]

subseq = ''

for i in range(0, len(first)):
    for j in range(i, len(first)):
        m = first[i:j]
        found = False
        for comp in compare:
            if m in comp:
                found = True
            else:
                found = False
                break
        if found and len(m) >= len(subseq):
            subseq = m

print(subseq)
