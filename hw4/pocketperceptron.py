import numpy
import copy
from perceptron import Perceptron
LEARNINGFACTOR = .5

class PocketPerceptron(Perceptron):
    def __init__(self, indim):
        Perceptron.__init__(self, indim)
        self.pocketweight = numpy.zeros(self.dim + 1)
        self.pocketerror = 1

    def digest(self, allrows, allvals):
        for i in range(len(allvals)):
            row = [1] + allrows[i]
            val = allvals[i]
            prediction = self.calcval(row)

            diff = val - prediction
            if (diff != 0):
                diff = self.stepfunc(diff)

            for j in range(len(self.weights)):
                self.weights[j] = self.weights[j] +  LEARNINGFACTOR * diff * row[j]

        error = self.getError(allrows, allvals)
        if error < self.pocketerror:
            self.pocketerror = error
            self.pocketweight = copy.deepcopy(self.weights)

    def finalize(self):
        self.weights = copy.deepcopy(self.pocketweight)
        print(self.weights)

    def getError(self, allrows, allvals):
        countwrong = 0
        for i in range(len(allvals)):
            row = allrows[i]
            val = allvals[i]
            prediction = self.predict(row)
            if val != prediction:
                countwrong += 1

        error = float(countwrong) / len(allvals)
        return error


