from Bio import SeqIO

seqs = []

for seq_record in SeqIO.parse("rosalind_tran.txt", "fasta"):
    seqs.append(str(seq_record.seq))

transitions = {
    'A': 'G',
    'G': 'A',
    'C': 'T',
    'T': 'C'
}

transversion_one = {
    'A': 'C',
    'C': 'A',
    'G': 'C',
    'T': 'A',
}

transversion_two = {
    'C': 'G',
    'A': 'T',
    'G': 'T',
    'T': 'G'
}
i = 0

transition_num = 0
transversion_num = 0

while i < len(seqs[0]):
    p1 = seqs[0][i]
    p2 = seqs[1][i]
    if transitions[p1] == p2:
        transition_num += 1
    if transversion_one[p1] == p2 or transversion_two[p1] == p2:
        transversion_num += 1
    i += 1

print(transition_num/transversion_num)
