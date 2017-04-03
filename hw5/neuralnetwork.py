import math


class NeuralNode:

    def __init__(self):
        self.inweights = []
        self.outweights = []
        #using bidirectional link so we can traverse forward and backwards easily
        #you can do it with stacks/recursion but this is easier for me
        self.ins = []
        self.outs = []
        self.x = 0
        self.theta = 0

    def addNext(self, next, weight):
        self.outs.append(next)
        self.outweights.append(weight)
        next.ins.append(self)
        next.inweights.append(weight)

    def calcX(self):
        x = 0
        for i in range(len(self.inweights)):
            contribution = self.inweights[i] * self.ins[i].x
            x += contribution
        self.x = sigmoid(x)

    def calcTheta(self):
        eps = 0
        x = self.x
        for i in range(len(self.outs)):
            w = self.outweights[i]
            thetaplus1 = self.outs[i].theta
            eps += w * thetaplus1
        theta = x * (1 - x) * eps
        self.theta = theta

    def isInput(self):
        return len(self.inweights) == 0

    def isOutput(self):
        return len(self.outs) == 0

    def updateWeights(self, rate):
        #we end up doing 2x more updates here because we have bi-directional weights...
        for i in range(len(self.ins)):
            w = self.inweights[i]
            x = self.ins[i].x
            theta = self.theta
            self.inweights[i] = w - rate * x * theta

        for i in range(len(self.outs)):
            w = self.outweights[i]
            x = self.x
            theta = self.outs[i].theta
            self.outweights[i] = w - rate * x * theta

class NNTrainer:
    def __init__(self, network, trainingset):
        self.trainset = trainingset
        self.network = network

    def train(self, epochs):
        for i in range(epochs):
            print('training epoch %d' % i)
            self.trainSingleEpoch()

    def trainSingleEpoch(self):
        for trainrow in self.trainset:
            self.trainSingleRow(trainrow)

    def trainSingleRow(self, row):
        img = row.inrow
        imgaslist = []
        for r in img:
            imgaslist  = imgaslist + r.tolist()
        e_out = row.outval
        self.network.stageInputs(imgaslist)
        self.network.feedforward()
        self.network.stageErrors([e_out])
        self.network.backPropagate()
        self.network.updateWeights()

class NNTester:
    def __init__(self, network, testset):
        self.set = testset
        self.network = network
        self.error = []

    def test(self):
        self.error = []
        for testrow in self.set:
            self.error.append(self.getSingleRowError(testrow))
        return self.error

    def getSingleRowError(self, row):
        img = row.inrow
        imgaslist = []
        for r in img:
            imgaslist = imgaslist + r.tolist()
        e_out = row.outval
        self.network.stageInputs(imgaslist)
        self.network.feedforward()
        x = self.network.outnodes[0].x
        diff = e_out - x
        return abs(diff)

    def getMeanAbsError(self):
        return sum(self.error) / float(len(self.set))

    def getRootMeanSquaredError(self):
        squared = [i**2 for i in self.error]
        s = sum(squared) / float(len(self.set))
        return math.sqrt(s)

class TrainingRow:
    def __init__(self, inputrow, outputval):
        self.inrow = inputrow
        self.outval = outputval

def sigmoid(s):
    try:
        es = math.exp(-s)
        return 1 / (1 + es)
    except OverflowError:
        #silly python precision...
        if(s < 0):
            return 0.0
        else:
            return 1.0
