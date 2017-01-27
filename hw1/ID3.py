__author__ = 'paul'
import nightoutdata
import  numpy
import math

class id3node:
    def __init__(self, name):
        self.isDecision = False
        self.name = name
        self.branches = []

def id3(rows, attributes, target):
    if(rows == None or len(rows) == 0):
        node = id3node('None')
        node.isDecision = True
        return node
    currentEntropy = getEntropy(rows, target)
    if(currentEntropy == 0):
        decision = rows[0].attr[target]
        node = id3node(decision)
        node.isDecision = True
        return node
    if(attributes == None or len(attributes) == 0):
        node = id3node(getMostTarget(rows, target))
        node.isDecision = True
        return node
    maxgain = 0
    maxindex = -1
    maxsplit = []
    for i in range(len(attributes)):
        (infoGain, split) = getInfoGain(rows, attributes[i], target, currentEntropy)
        if(infoGain > maxgain):
            maxgain = infoGain
            maxindex = i
            maxsplit = split
    maxattr = attributes[maxindex]
    node = id3node(maxattr)
    newattributes = getNewAttributesCopy(attributes, maxattr)
    for i in range(len(nightoutdata.attributes[maxattr])):
        node.branches.append(id3(maxsplit[i], newattributes, target))
    return node



def getNewAttributesCopy(attributes, minus):
    result = []
    for attribute in attributes:
        if(attribute != minus):
            result.append(attribute)
    return result

def getInfoGain(rows, attribute, target, currentEntropy):
    fromAttr = 0.
    split = splitData(rows, attribute)
    for subset in split:
        if(len(subset) > 0):
            contribution = float(len(subset))/len(rows) * getEntropy(subset, target)
            fromAttr += contribution
    return (currentEntropy - fromAttr, split)

def splitData(rows, attribute):
    result = []
    for i in range(len(nightoutdata.attributes[attribute])):
        result.append([])
    for row in rows:
        index = nightoutdata.attributes[attribute].index(row.attr[attribute])
        result[index].append(row)
    return result

def getMostTarget(rows, target):
    sizeTarget = len(nightoutdata.attributes[target])
    results = numpy.zeros(sizeTarget).astype(int)
    for row in rows:
        outcome = row.attr[target]
        index = nightoutdata.attributes[target].index(outcome)
        results[index]+=1
    cmax = 0
    cindex = -1
    for i in range(len(results)):
        result = results[i]
        if(result > cmax):
            cmax = result
            cindex = i
    return nightoutdata.attributes[target][cindex]

def getEntropy(rows, target):
    sizeOutcome = len(nightoutdata.attributes[target])
    results = numpy.zeros(sizeOutcome).astype(int)

    for row in rows:
        outcome = row.attr[target]
        outindex = nightoutdata.attributes[target].index(outcome)
        results[outindex]+=1
    return entropyOfSums(results,len(rows))

def entropyOfSums(sums, total):
    entropy = 0.

    for i in range(len(sums)):
        p = sums[i] / float(total)
        if(p!=0):
            contribution = p * math.log(p, 2)
            entropy -= contribution

    return entropy

def isInFilter(row, given):
    if(given):
        for key in given:
            if row.attr[key] != given[key]:
                return False
        return True
    else:
        return True

def isPure(rows, target):
    test = rows[0].attr[target]
    for row in rows:
        if(test != row.attr[target]):
            return False
    return True

def getDecision(row, root):
    if(root.isDecision):
        return root.name
    tobranch = row.attr[root.name]
    index = nightoutdata.attributes[root.name].index(tobranch)
    return getDecision(row, root.branches[index])