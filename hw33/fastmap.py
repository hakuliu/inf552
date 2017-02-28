__author__ = 'paul'

import fastmapparser
import random
import numpy

TARGETDIM = 2

def getMaxDistFor(objIndex, distances):
    maxIndex = 0
    maxDist = 0
    for i in range(len(distances)):
        if(distances[objIndex,i] > maxDist):
            maxDist = distances[objIndex,i]
            maxIndex = i
    return maxIndex

def getPivots(distances):
    size = len(distances)
    a = random.randint(0,size-1)
    b = getMaxDistFor(a,distances)
    a = getMaxDistFor(b,distances)
    #do it one more time just to be sure
    b = getMaxDistFor(a,distances)
    a = getMaxDistFor(b,distances)
    return a,b

class FastMapper:

    def __init__(self, n):
        self.n = n
        self.images = numpy.zeros((self.n,TARGETDIM))
        self.pivots = numpy.zeros((2,TARGETDIM))
        self.col = -1

    def fastMap(self, dim,distances):
        if dim <= 0:
            return
        else:
            self.col+=1
        piva, pivb = getPivots(distances)
        self.pivots[0,self.col] = piva
        self.pivots[1,self.col] = pivb
        if(distances[piva,pivb] == 0):
            self.images[:,self.col] = 0
        self.fastMap(dim - 1, distances)





O = fastmapparser.parsefile('fastmap-data.txt')
#print(O)
mapper = FastMapper(len(O))
mapper.fastMap(TARGETDIM, O)