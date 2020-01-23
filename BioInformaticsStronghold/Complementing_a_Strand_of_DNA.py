listDNA = "AAAACCCGGT"


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


result = ''.join(list(map(complement, listDNA[::-1])))

print(result)
