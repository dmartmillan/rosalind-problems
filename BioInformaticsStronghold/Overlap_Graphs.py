import networkx as nx
from Bio import SeqIO

G = nx.DiGraph()

seq_DNA = {}

for seq_record in SeqIO.parse("rosalind_grph.txt", "fasta"):
    G.add_node(seq_record.id)
    seq_DNA[seq_record.id] = str(seq_record.seq)

for i in seq_DNA.keys():
    for j in seq_DNA.keys():
        if i != j:
            if seq_DNA[i][-3:] == seq_DNA[j][:3]:
                G.add_edge(i, j)

nx.write_edgelist(G, "edge_list.txt", data=False)
