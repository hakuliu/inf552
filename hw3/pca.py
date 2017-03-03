import numpy

def doPCA(data, dim):
    data = makeDataMatrix(data)
    means = getMeanVector(data)
    data = normalizeData(data, means)
    cov = getCov(data)
    eigvals, eigvecs = getEigs(cov)
    principalComponents = sortEigs(eigvals, eigvecs)
    return getDimensions(dim, principalComponents)


def getDimensions(d, pc):
    if d <= len(pc):
        result = numpy.zeros((d, len(pc[0])))
        for i in range(d):
            result[i] = pc[:,i]
        return result
    else: return None

def sortEigs(vals, vecs):
    result = numpy.zeros((len(vecs), len(vecs[0])))
    #selection sort because vals is short for now so it should be fast enough
    lastMax = float("inf")
    for i in range(len(vals)):
        currentMax = float("-inf")
        currentInd = -1
        for j in range(len(vals)):
            if vals[j] > currentMax and vals[j] < lastMax:
                currentMax = vals[j]
                currentInd = j
        if currentInd != -1:
            result[i] = vecs[currentInd]
            lastMax = currentMax
    return result

def getEigs(cov):
    return numpy.linalg.eig(cov)

def getCov(data):
    return numpy.cov(data)

def getMeanVector(data):
    result = numpy.zeros(len(data))
    for i in range(len(data)):
        result[i] = numpy.mean(data[i,:])
    return result

def normalizeData(data, means):
    result = numpy.zeros((len(data), len(data[0])))
    for i in range(len(data)):
        result[i] = data[i,:] - means[i]
    return result

def makeDataMatrix(data):
    return numpy.transpose(data)