import neuralnetwork
import random
from collections import deque


class FeedForwardNetwork:
    def __init__(self, indim, outdim, hiddendim):
        self.indim = indim
        self.outdim = outdim
        self.hiddendim = hiddendim
        self.innodes = []
        self.outnodes = []
        self.allLayers = []
        self.learnrate = .1

    def constructNetwork(self):
        currentlayer = []
        for i in range(self.indim):
            node = neuralnetwork.NeuralNode()
            self.innodes.append(node)
        currentlayer = self.innodes
        self.allLayers.append(self.innodes)
        alldims = [] + self.hiddendim + [self.outdim]
        for dim in alldims:
            print('constructing layer of %d nodes' % dim)
            nextlayer = []
            for a in range(dim):
                nextlayer.append(neuralnetwork.NeuralNode())
            for a in currentlayer:
                for b in nextlayer:
                    a.addNext(b, self.makeInitialWeight())
            self.allLayers.append(nextlayer)
            currentlayer = nextlayer
        self.outnodes = nextlayer

    def makeInitialWeight(self):
        return random.uniform(-1, 1)

    def stageInputs(self, inrow):
        if len(inrow) != len(self.innodes):
            raise ValueError('input not the same size as expected')
        for i in range(len(self.innodes)):
            self.innodes[i].x = inrow[i]

    def feedforward(self):
        q = deque()
        for layer in self.allLayers:
            for node in layer:
                q.append(node)

        for node in q:
            if not node.isInput():
                node.calcX()

    def stageErrors(self, expectedout):
        if len(expectedout) != len(self.outnodes):
            raise ValueError('output not the same size as expected')
        normfactor = 1.0 / self.outdim
        for i in range(len(self.outnodes)):
            x = self.outnodes[i].x
            y = expectedout[i]
            diff = x - y
            theta = normfactor * 2 * diff * x * (1 - x)
            self.outnodes[i].theta = theta

    def backPropagate(self):
        q = deque()
        for layer in reversed(self.allLayers):
            for node in layer:
                q.append(node)

        for node in q:
            if not node.isOutput():
                node.calcTheta()

    def updateWeights(self):
        q = deque()
        for layer in self.allLayers:
            for node in layer:
                q.append(node)
        for node in q:
            node.updateWeights(self.learnrate)