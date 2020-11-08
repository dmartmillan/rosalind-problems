from Bio import SeqIO

MIN_LEN = 4
MAX_LEN = 12

seq_DNA = []
seq_DNA_aux = []

pairs = {
    'T': 'A',
    'A': 'T',
    'C': 'G',
    'G': 'C'
}


def is_palindrome(seq, seq_rev):
    palindrome = True
    for y, subs in enumerate(seq):
        palindrome = (pairs[subs] == seq_rev[y])
        if not palindrome:
            break
    return palindrome


for seq_record in SeqIO.parse("rosalind_revp.txt", "fasta"):
    seq_DNA = [char for char in str(seq_record.seq)]
    for i, acid in enumerate(seq_DNA):
        for x in range(MIN_LEN, MAX_LEN + 1):
            seq_DNA_aux = seq_DNA[i:i + x]
            if len(seq_DNA_aux) == x:
                seq_DNA_aux_rev = seq_DNA_aux.copy()
                seq_DNA_aux_rev.reverse()
                if is_palindrome(seq_DNA_aux, seq_DNA_aux_rev):
                    print(i + 1, len(seq_DNA_aux))
