from Bio import SeqIO
from math import factorial


def perfect_match(rna):
    AU = rna.count('A')
    GC = rna.count('G')
    print(factorial(AU) * factorial(GC))


for seq_record in SeqIO.parse("rosalind_pmch.txt", "fasta"):
    perfect_match(str(seq_record.seq))
