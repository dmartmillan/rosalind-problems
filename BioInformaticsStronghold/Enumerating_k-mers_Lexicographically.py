symbols = 'A B C D E F G H'
n = 3


def combinations(seq, n, sub_seq = '', seq_list = []):
    if n == 0:
        seq_list.append(sub_seq)
    else:
        for s in seq:
            combinations(seq, n - 1, sub_seq + s, seq_list)
    return seq_list


symbols = symbols.split(' ')

sub_seq = ''

for s in combinations(symbols, n):
    print(s)
