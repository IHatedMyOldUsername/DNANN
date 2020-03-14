with open('output.txt') as inputFile:
    lineFile = inputFile.readlines()

ct = 0
balIn = np.array([])
for line in lineFile:
    if(len(line)  36):
        continue
    endArray = np.array([])
    for char in line:
        if(char == '\n'):
            continue
        endArray = np.append(endArray, int(char))
    ct += 1
    balIn = np.append(balIn, endArray, axis = 0)
    print(str(round(100-(ct/len(lineFile)), 3)) + '% left',end='\r')

np.save('finalInput.npy', balIn)
