import numpy as np

with open('output.txt') as inputFile:
    lineFile = inputFile.readlines()

ct = 0
balIn = []
print(len(lineFile))
for line in lineFile:
    if(len(line)-1 != 36): #If the length is wrong, stop it!
        continue
    endList = list()
    for char in line.rstrip():
        endList += [char]
    balIn += [np.asarray(endList)]
    ct+=1
    if(ct >= 11842900):
        continue

finalOut = np.asarray(balIn)
np.save('finalInput.npy', balIn)
