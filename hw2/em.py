import numpy
import random

def em(points, k):
    minmax = getMinMax(points)
    gausses = initSeeds(k, minmax)
    assignments = PointAssignment.initAssignments(points, k)
    changed = True
    while(changed):
        changed = iterateAssignments(assignments, gausses)
        gausses = updateGausses(assignments, gausses)
    return gausses, assignments

def updateGausses(assignments, gausses):
    #get membership of weights
    for j in range(len(gausses)):
        gausses[j].membership = 0

    for i in range(len(assignments)):
        row = assignments[i]
        for j in range(len(gausses)):
            gauss = gausses[j]
            gauss.membership = gauss.membership + row.weights[j]

    #update values
    total = len(assignments)
    for j in range(len(gausses)):
        gauss = gausses[j]
        gauss.intensity = gauss.membership / total
        gauss.mean = getNewMean(assignments, gauss, j)
        gauss.covar = getNewCovar(assignments, gauss, j)
    return gausses

def getNewMean(assignments, gauss, j):
    normalization = 1 / gauss.membership
    xmean = 0
    ymean = 0
    for i in range(len(assignments)):
        assignment = assignments[i]
        xmean = xmean + assignment.weights[j] * assignment.point[0]
        ymean = ymean + assignment.weights[j] * assignment.point[1]
    xmean = normalization * xmean
    ymean = normalization * ymean
    return [xmean, ymean]


def getNewCovar(assignments, gauss, j):
    normalization = 1 / gauss.membership
    newcovar = numpy.matrix([[0,0],[0,0]])
    for i in range(len(assignments)):
        assignment = assignments[i]
        ric = assignment.weights[j]

        xdiff = assignment.point[0] - gauss.mean[0]
        ydiff = assignment.point[1] - gauss.mean[1]
        diff = numpy.matrix([xdiff,ydiff])
        ricdiffT = numpy.matrix([[ric * xdiff],
                                 [ric * ydiff]])
        contribution = numpy.dot(ricdiffT, diff)
        newcovar = numpy.add(newcovar, contribution)
    newcovar = numpy.dot(normalization, newcovar)
    return newcovar



def iterateAssignments(assignments, gausses):
    changed = False
    for i in range(len(assignments)):
        point = assignments[i]
        prevassignment = point.getAssignment()
        for j in range(len(gausses)):
            gauss = gausses[j]
            pGivenC = normOfPointUnderC(point.point, gauss)
            point.probGivenC[j] = pGivenC
        for j in range(len(gausses)):
            gauss = gausses[j]
            weight = getWeight(point, j)
            point.weights[j] = weight
        if(prevassignment != point.getAssignment()):
            changed = True
    return changed

def getWeight(point, j):
    ric = point.probGivenC[j]
    ric = ric / point.getSumProbs()
    return ric


def normOfPointUnderC(point, gauss):
    normalization = 2 * numpy.pi
    normalization = normalization +numpy.linalg.norm(gauss.covar)
    normalization = numpy.sqrt(normalization)
    normalization = 1/normalization

    xdiff = point[0] - gauss.mean[0]
    ydiff = point[1] - gauss.mean[1]

    diff = numpy.matrix([[xdiff],
                         [ydiff]])
    nhalfdiffT = numpy.matrix([-.5 * xdiff, -.5 * ydiff])
    invcovar = numpy.linalg.inv(gauss.covar)
    p = numpy.dot(invcovar, diff)
    p = numpy.dot(nhalfdiffT, p)
    p = numpy.exp(p)
    p = normalization * p
    return p




#omit sqrt for speed
def dist(point1, point2):
    xdiff = point1[0] - point2[0]
    ydiff = point1[1] - point2[1]
    return xdiff * xdiff + ydiff * ydiff

def getMinMax(points):
    xmin = points[0][0]
    xmax = points[0][0]
    ymin = points[0][1]
    ymax = points[0][1]
    for i in range(len(points)):
        point = points[i]
        if (point[0] < xmin):
            xmin = point[0]
        if (point[0] > xmax):
            xmax = point[0]
        if (point[1] < ymin):
            ymin = point[1]
        if (point[1] > ymax):
            ymax = point[1]
    return [[xmin, ymin], [xmax, ymax]]


def initSeeds(k, minmax):
    seeds = []
    for i in range(k):
        x = random.uniform(minmax[0][0],minmax[1][0])
        y = random.uniform(minmax[0][1],minmax[1][1])
        seeds.append(Gauss(x,y))
    return seeds

class Gauss:
    def __init__(self, x, y):
        self.mean = [x,y]
        self.membership = 0
        self.intensity = 1
        self.covar = numpy.matrix([[1,0],[0,1]])

class PointAssignment:
    def __init__(self, point, k):
        self.point = point
        self.probGivenC = numpy.zeros(k)
        self.weights = numpy.zeros(k)

    def getAssignment(self):
        maxindex = 0
        maxweight = 0
        for i in range(len(self.weights)):
            if(self.weights[i] > maxweight):
                maxindex = i
                maxweight = self.weights[i]
        return maxindex

    def getSumProbs(self):
        sum = 0.
        for i in range(len(self.probGivenC)):
            sum += self.probGivenC[i]
        return sum

    @classmethod
    def initAssignments(cls, points, k):
        assignments = []
        for i in range(len(points)):
            assignments.append(PointAssignment(points[i], k))
        return assignments
