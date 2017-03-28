import cv2
from neuralnetwork import TrainingRow
import itertools


def makeTrainingSet(trainlistfilename):
    f = open(trainlistfilename, 'r')
    result = []
    for imgfilename in f:
        outval = 0
        if "down" in imgfilename:
            outval = 1
        im = cv2.imread(imgfilename.strip(), -1)
        im = im / float(32)
        result.append(TrainingRow(im, outval))
    return result

def makecsvfile(rows, outfilename):
    f = open(outfilename, 'w')
    im = rows[0].inrow
    imgaslist = []
    for r in im:
        imgaslist = imgaslist + r.tolist()

    header = ''
    for i in range(len(imgaslist)):
        header += 'x'+str(i)+','
    header += 'out\n'
    f.write(header)

    for row in rows:
        line = ''
        imgaslist = []
        for r in row.inrow:
            imgaslist = imgaslist + r.tolist()
        for i in range(len(imgaslist)):
            line += str(imgaslist[i]) + ','
        line += str(row.outval)+'\n'
        f.write(line)
