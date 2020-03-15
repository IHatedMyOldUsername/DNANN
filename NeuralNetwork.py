import numpy as np
import random as rand

class dnaBrain(object):
    def __init__(self):
        self.inputSize = 34 ##5 Amino Acids, 1=A, 2=C, etc.
        self.outputSize = 1 ##Output prediction
        self.hiddenSize = 20 ##Middle Neurons

        self.W1 = np.random.randn(self.inputSize, self.hiddenSize)
        self.W2 = np.random.randn(self.hiddenSize, self.outputSize)


    def forward(self, X):
        X = X.astype('float64')
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = self.sigmoid(self.z3)
        return yHat

    def backward(self, X, y, o):
        self.o_error = y - o
        self.o_delta = self.o_error*self.sigmoidPrime(o)

        self.z2_error = self.o_delta.dot(self.W2.T)
        self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2)

        self.W1 += X.T.dot(self.z2_delta)
        self.W2 += self.z2.T.dot(self.o_delta)
    
    def train(self,X, y):
        O = self.forward(X)
        self.backward(X, y, o)

    def sigmoid(self, z):
        return 1/(1+np.exp(-z))
    
    def sigmoidPrime(self, s):
        return s*(1-s)

data = np.load('~/Documents/finalInput.npy', allow_pickle=True)
neuralNet = dnaBrain()

