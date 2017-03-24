import numpy
import copy
import math
from perceptron import Perceptron

LEARNINGRATE = 1.0
class LogisticRegression(Perceptron):
    def __init__(self, indim):
        Perceptron.__init__(self, indim)

    def digest(self, allrows, allvals):
        #row = [1] + row
        #if len(row) != len(self.weights):
        #    return []
        learning = self.calclearning(allrows, allvals)
        for i in range(len(self.weights)):
            self.weights[i] += (LEARNINGRATE / len(allvals)) * learning[i]

    def calclearning(self, allrows, allvals):
        sum = numpy.zeros(self.dim + 1)
        for i in range(len(allvals)):
            yi = allvals[i]
            xi = [1] + allrows[i]
            pi = self.calcexp(xi, yi)
            for j in  range(len(sum)):
                sum[j] += xi[j] * yi * pi
        return sum

    def calcexp(self, rowplus1, yi):
        val = 0
        for i in range(len(self.weights)):
            val += self.weights[i] * rowplus1[i]
        val *= yi
        es = math.exp(val)
        return  1/ (1 + es)

    def calcval(self, rowplus1):
        val = 0
        for i in range(len(self.weights)):
            val += self.weights[i] * rowplus1[i]
        es = math.exp(val)
        return es / (1 + es)

#[-0.03150075 -0.17769619  0.11445235  0.07670126]

