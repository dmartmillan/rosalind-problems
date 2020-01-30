from Bio import SeqIO

profile_Matrix = {"A": [], "C": [], "G": [], "T": []}

for seq_record in SeqIO.parse("rosalind_cons.txt", "fasta"):
    for i, symbol in enumerate(str(seq_record.seq)):
        consensusResult = profile_Matrix[symbol]
        lengthSeq = len(str(seq_record.seq))
        if len(consensusResult) == 0:
            consensusResult = [0] * lengthSeq
        consensusResult[i] += 1
        profile_Matrix[symbol] = consensusResult

consensus = [0] * lengthSeq
for i in range(0, lengthSeq):
    maxim = 0
    for j in profile_Matrix.keys():
        if maxim < profile_Matrix[j][i]:
            consensus[i] = j
            maxim = profile_Matrix[j][i]


result = ''.join([str(v) for v in consensus])

f = open("rosalind_cons_result.txt", "w")
f.write(result + '\n')
for j in profile_Matrix.keys():
    profile = ' '.join([str(v) for v in profile_Matrix[j]])
    f.write(j + ': ' + profile + '\n')
f.close()
