with open('input.txt') as inputFile:
    cleanInput = inputFile.readlines()

strandNumber = 0
strandOut = []
for strand in cleanInput:
    if not strand == '\n':
        endString = ''
        for char in strand:
            if char == 'A':
                endString = endString + '1'
            elif char == 'C':
                endString = endString + '2'
            elif char == 'G':
                endString = endString + '3'
            elif char == 'T':
                endString = endString + '4'
        with open('output.txt', 'a') as out:
            out.write(endString + '\n')

    strandNumber += 1
    print(str(round(strandNumber/len(cleanInput)*100, 3)) + '/% analyses completed.', end='\r')