f = open("rosalind_tree.txt", "r")

n = 0
components = []

first = True

for x in f:
    if first:
        n = int(x)
        first = False
        for n in range(1, n + 1):
            adjnode = set()
            adjnode.add(n)
            components.append(adjnode)
    else:
        nodes = [int(s) for s in x.rstrip().split(' ')]
        last = 0
        for i, com in enumerate(components):
            if nodes[0] in com:
                last = i
                for n in nodes:
                    com.add(n)

        for n in nodes:
            for i, com in enumerate(components):
                if n in com and i != last:
                    union = set.union(components[last], com)
                    components[last] = union
                    if i < last:
                        last -= 1
                    components.remove(com)

#print(components)
print(len(components) - 1)
