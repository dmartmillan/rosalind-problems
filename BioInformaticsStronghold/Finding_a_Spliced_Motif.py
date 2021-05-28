from Bio import SeqIO

seqs = []

for seq_record in SeqIO.parse("rosalind_sseq.txt", "fasta"):
    seqs.append(str(seq_record.seq))

result = ""

s = 0
for t in seqs[1]:
    while s < len(seqs[0]):
        if seqs[0][s] == t:
            result = result + str(s + 1) if len(result) == 0 else result + ' ' + str(s + 1)
            s += 1
            break
        else:
            s += 1

print(result)
