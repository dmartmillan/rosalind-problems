from Bio import SeqIO


def overlaps(arr, acc=''):
    if len(arr) == 0:
        return acc
    elif len(acc) == 0:
        acc = arr.pop(0)
        return overlaps(arr, acc)
    else:
        for i in range(len(arr)):
            a = arr[i]
            l = len(a)

            for p in range(int(l / 2)):
                q = l - p
                if acc.startswith(a[p:]):
                    arr.pop(i)
                    return overlaps(arr, a[:p] + acc)
                if acc.endswith(a[:q]):
                    arr.pop(i)
                    return overlaps(arr, acc + a[q:])


seq_dna = ''
all_seq = []

for seq_record in SeqIO.parse("rosalind_long.txt", "fasta"):
    all_seq.append(str(seq_record.seq))

print(overlaps(all_seq))
