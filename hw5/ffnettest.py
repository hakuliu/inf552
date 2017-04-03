__author__ = 'paul'
from ffnet import ffnet, mlgraph
import numpy


infile = 'wekadata.csv'
testfile = 'wekadatatest.csv'

inputnum = 32*30
inrownum = 184
testrownum = 83

def readin(filename, rows):
    f = open(filename, 'r')
    input = numpy.zeros((rows, inputnum))
    target = numpy.zeros((rows, 1))
    headerskipped = False
    i = 0
    for line in f:
        if(headerskipped):
            line = line.split(',')
            last = len(line) - 1
            instr = line[0:last]
            inline = []
            for j in range(len(instr)):
                x = float(instr[j])
                input[i,j] = x
            target[i,0] = float(line[last].strip())
            i+=1
        else:
            headerskipped = True

    f.close()
    return input,target


input,target = readin(infile, inrownum)

testin,testtarget = readin(testfile, testrownum)

connections = mlgraph((inputnum, 100, 1))
net = ffnet(connections)

print('training net...')
#net.train_momentum(input, target, eta=0.5, momentum=.1)
net.train_tnc(input, target)
print('testing net...')
output, regression = net.test(testin, testtarget, iprint = 2)
print(output)
print(regression)