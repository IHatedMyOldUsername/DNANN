import numpy as np

with open('output.txt') as inputFile:
    lineFile = inputFile.readlines()

ct = 0
balIn = np.array([])
print(len(lineFile))
for line in lineFile:
    if(len(line)-1 != 36): #If the length is wrong, stop it!
        continue
    endArray = np.array([])
    for char in line.rstrip():
        endArray = np.append(endArray, int(char))
    balIn = np.append(balIn, endArray, axis = 0)

np.save('finalInput.npy', balIn)
print(balIn)
