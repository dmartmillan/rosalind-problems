fileDNA = open("rosalind_gc.txt", "r")

linesFile = fileDNA.readlines()

maximGCname = ''
maximGCvalue = 0

countC, countG = 0, 0
seqDNA = ""
name = ""

for line in linesFile:
    if line[0] == '>':
        if len(seqDNA) > 0:
            cgValue = (countC + countG) / len(seqDNA) * 100
            if cgValue > maximGCvalue:
                maximGCvalue = cgValue
                maximGCname = name
        name = line.replace('\n', '')
        seqDNA = ""
        countG, countC = 0, 0
    else:
        seqDNA += line.replace('\n', '')
        countG += line.count('C')
        countC += line.count('G')

if len(seqDNA) > 0:
    cgValue = (countC + countG) / len(seqDNA) * 100
    if cgValue > maximGCvalue:
        maximGCvalue = cgValue
        maximGCname = name

print(maximGCname)
print(maximGCvalue)

