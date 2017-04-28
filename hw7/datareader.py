def readData(file):
    f = open(file, 'r')
    result = []
    for line in f:
        l = line.strip().split(',')
        x = float(l[0])
        y = float(l[1])
        v = int(l[2])
        result.append(DataPoint(x, y, v))
    return result

class DataPoint:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val


def writecsv(fname, data):
    f = open(fname, 'w')
    for d in data:
        yesno = "yes"
        if d.val < 0: yesno = "no"
        f.write(str(d.x)+","+str(d.y)+","+yesno+"\n")

data = readData('nonlinsep.txt')
writecsv('nonlinsep.csv', data)