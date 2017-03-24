import numpy
LEARNRATE = .5
class Perceptron:
    def __init__(self, indim):
        self.dim = indim
        self.weights = numpy.zeros(self.dim + 1)

    def digest(self, row, desiredval):
        row = [1] + row
        if len(row) != len(self.weights):
            return []
        expected = self.calcval(row)
        diff = desiredval - expected
        if(diff != 0):
            diff = self.stepfunc(diff)
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + LEARNRATE * diff * row[i]

    def predict(self, row):
        row = [1] + row
        return self.calcval(row)

    def calcval(self, rowplus1):

        val = 0
        for i in range(len(self.weights)):
            val += self.weights[i] * rowplus1[i]
        return self.stepfunc(val)

    def stepfunc(self, val):
        if val > 0:
            return 1
        else:
            return -1