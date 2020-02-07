import requests
from Bio import SeqIO
import re
import os

fileIDs = open('rosalind_mprt.txt', 'r')
proteinsIDs = list(map(lambda x: x.replace('\n', ''), fileIDs.readlines()))

proteinsDataIDS = []

fileProteins = open("protein_results.txt", "w")

for id in proteinsIDs:
    result = requests.get('https://www.uniprot.org/uniprot/' + str(id) + '.fasta')
    if result.ok:
        proteinsDataIDS.append(id)
        fileProteins.write(result.text)
    else:
        print('Protein', id, 'not found')

fileProteins.close()
fileIDs.close()

for i, seq_record in enumerate(SeqIO.parse("protein_results.txt", "fasta")):
    motif = ""
    first = True
    p = re.compile(r'(?=(N[^P][ST][^P]))')
    for m in p.finditer(str(seq_record.seq)):
        if first:
            first = False
            motif += str(m.start() + 1)
        else:
            motif += " " + str(m.start() + 1)

    if len(motif) > 0:
        print(proteinsDataIDS[i])
        print(motif)

os.remove("protein_results.txt")
