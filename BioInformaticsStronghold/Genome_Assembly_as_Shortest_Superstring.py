from Bio import SeqIO

seq_dna = ''
first = True

for seq_record in SeqIO.parse("example.txt", "fasta"):
    if first:
        seq_dna = str(seq_record.seq)
        first = False
    else:
        found = False
        for i in seq_dna:
            for j in str(seq_record.seq):
                print(i, j)
