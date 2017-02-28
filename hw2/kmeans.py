import numpy
import random

def kmeans(points, k):
    minmax = getMinMax(points)
    centroids = initSeeds(k, minmax)
    assignments = numpy.zeros(len(points)).astype(int)
    changed = True
    while changed:
        changed = iterateAssignments(points, assignments, centroids)
        if changed:
            centroids = changeCentroids(points, assignments, centroids)
    return centroids, assignments

def changeCentroids(points, assignments, centroids):
    counts = numpy.zeros(len(centroids))
    sums = numpy.zeros((len(centroids), 2))
    for i in range(len(points)):
        point = points[i]
        assignment = assignments[i]
        counts[assignment] += 1
        for j in range(len(sums[0])):
            sums[assignment][j] += point[j]

    for i in range(len(sums)):
        if counts[i] == 0:
            centroids[i] = centroids[i]
        else:
            centroids[i] = [sums[i][0] / counts[i], sums[i][1] / counts[i]]
    return centroids

def iterateAssignments(points, assignments, centroids):
    changed = False
    for i in range(len(points)):
        point = points[i]
        closestIndex = 0
        closestDist = dist(point, centroids[0])
        for j in range(len(centroids)):
            d = dist(point, centroids[j])
            if(d < closestDist):
                closestDist = d
                closestIndex = j
        if(assignments[i] != closestIndex):
            changed = True
        assignments[i] = closestIndex
    return changed

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
        seeds.append([x,y])
    return seeds
