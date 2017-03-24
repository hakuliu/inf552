import numpy

def getW(d, y):
    dt = numpy.transpose(d)
    ddt = numpy.matmul(d,dt)
    ddtinv = numpy.linalg.inv(ddt)
    result = numpy.matmul(ddtinv, d)
    result = numpy.matmul(result, y)
    return result