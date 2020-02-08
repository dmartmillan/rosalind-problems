from Bio import SeqIO

codonDNATable = {
    "TTT": "F", "CTT": "L", "ATT": "I", "GTT": "V",
    "TTC": "F", "CTC": "L", "ATC": "I", "GTC": "V",
    "TTA": "L", "CTA": "L", "ATA": "I", "GTA": "V",
    "TTG": "L", "CTG": "L", "ATG": "M", "GTG": "V",
    "TCT": "S", "CCT": "P", "ACT": "T", "GCT": "A",
    "TCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "TCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "TCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
    "TAT": "Y", "CAT": "H", "AAT": "N", "GAT": "D",
    "TAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "TAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
    "TAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
    "TGT": "C", "CGT": "R", "AGT": "S", "GGT": "G",
    "TGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
    "TGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
    "TGG": "W", "CGG": "R", "AGG": "R", "GGG": "G", }

global proteinResults

proteinResults = set()


def transcript_dna_to_protein(seq):
    for i in range(0, len(seq)):
        if "ATG" == seq[i:i + 3]:
            protein = "M"
            for j in range(i + 3, len(seq), 3):
                if len(seq[j:j + 3]) < 3:
                    break
                sub_protein = codonDNATable[seq[j:j + 3]]
                if not sub_protein:
                    break
                elif "Stop" == sub_protein:
                    proteinResults.add(protein)
                    break
                else:
                    protein += sub_protein


def complement(value):
    if value == 'T':
        return 'A'
    elif value == 'A':
        return 'T'
    elif value == 'C':
        return 'G'
    elif value == 'G':
        return 'C'
    else:
        pass


def complement_dna(seq):
    return ''.join(list(map(complement, seq[::-1])))


for seq_record in SeqIO.parse("rosalind_orf.txt", "fasta"):
    transcript_dna_to_protein(str(seq_record.seq))
    transcript_dna_to_protein(complement_dna(str(seq_record.seq)))

for protein in proteinResults:
    print(protein)
