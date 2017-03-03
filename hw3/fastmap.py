__author__ = 'paul'

import random
import numpy

TARGETDIM = 2

class FastMapper:

    def __init__(self, distances):
        self.distances = distances.copy()
        self.n = len(distances)
        self.images = numpy.zeros((self.n,TARGETDIM))
        self.pivots = numpy.zeros((2,TARGETDIM))
        self.col = -1

    def fastMap(self, dim):
        if dim <= 0:
            return
        else:
            self.col+=1
        piva, pivb = self.getPivots()
        self.pivots[0,self.col] = piva
        self.pivots[1,self.col] = pivb
        if(self.distances[piva,pivb] == 0):
            self.images[:,self.col] = 0
        else:
            for i in range(self.n):
                xi = self.findProjectedPosition(piva,pivb,i)
                self.images[i,self.col] = xi
        self.updateDistances()
        self.fastMap(dim - 1)

    def findProjectedPosition(self,a,b,i):
        dai = self.distances[a,i]
        dab = self.distances[a,b]
        dbi = self.distances[b,i]
        numerator = dai**2 + dab**2 - dbi**2
        denominator = 2 * dab
        xi = numerator / denominator
        return xi

    def updateDistances(self):
        for i in range(self.n):
            for j in range(self.n):
                dprime = self.distances[i,j]**2 - (self.images[i,self.col] - self.images[j,self.col])**2
                self.distances[i,j] = dprime

    def getMaxDistFor(self,objIndex):
        maxIndex = 0
        maxDist = 0
        for i in range(len(self.distances)):
            if (self.distances[objIndex, i] > maxDist):
                maxDist = self.distances[objIndex, i]
                maxIndex = i
        return maxIndex

    def getPivots(self):
        size = len(self.distances)
        a = random.randint(0, size - 1)
        b = self.getMaxDistFor(a)
        a = self.getMaxDistFor(b)
        # do it one more time just to be sure
        b = self.getMaxDistFor(a)
        a = self.getMaxDistFor(b)
        return a, b

    def writeFile(self, filename):
        f = open(filename, 'w')
        for i in range(len(self.images)):
            image = self.images[i]
            f.write(str(i+1) + "," + str(image[0]) + "," + str(image[1]) + '\n')
        f.close()