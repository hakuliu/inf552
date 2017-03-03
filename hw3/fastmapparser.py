__author__ = 'paul'
import numpy


def parsefile(filepath):
    result = numpy.zeros((10,10))
    for line in open(filepath, 'r'):
        row = parseline(line)
        a = int(row[0]) - 1
        b = int(row[1]) - 1
        val = row[2]
        result[a,b] = val
        result[b,a] = val
    return result

def parseline(line):
    thesplit = line.split('\t')
    return thesplit

def parsewords(filepath):
    result = []
    for line in open(filepath, 'r'):
        result.append(line)
    return result