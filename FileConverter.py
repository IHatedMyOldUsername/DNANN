with open('input.fastq') as DirtyData:
    linedData = DirtyData.readlines()

testData = []
for line in linedData:
    if line[0] == '@':
        sig = True
        continue
    if sig:
        sig = False
        testData.append(line)

for term in testData:
    with open('input.txt', 'a') as inputFile:
        inputFile.write(term)