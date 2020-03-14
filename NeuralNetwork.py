import numpy as np
import curses

class dnaBrain(object):
    def __init__(self):
        self.inputSize = 30 ##5 Amino Acids, 1=A, 2=C, etc.
        self.outputSize = 1 ##Output prediction
        self.hiddenSize = 20 ##Middle Neurons

        self.W1 = np.random.randn(self.inputSize, self.hiddenSize)
        self.W2 = np.random.randn(self.hiddenSize, self.outputSize)
    
    def forward(self, X):
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = self.sigmoid(self.z3)
        return yHat
    
    def sigmoid(self, z):
        return 1/(1+np.exp(-z))

#NN = dnaBrain()
#yHat = NN.forward(balIn)
#print(yHat)