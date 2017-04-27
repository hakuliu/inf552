import datareader as dr
import svm
import matplotlib.pyplot as plot
import numpy as np

def extract(data, cl=1):
    x = []
    y = []

    for d in data:
        if d.val == cl:
            x.append(d.x)
            y.append(d.y)

    return x,y

linData = dr.readData('linsep.txt')
print(linData)

linsvm = svm.SVM(linData)
w,b = linsvm.train()

print(w)
print(b)

correctRate = linsvm.test(linData)

print('percent correct')
print(correctRate)

px, py = extract(linData, +1)
nx, ny = extract(linData, -1)
lx = np.linspace(0,.6,100)
ly = []
for x in lx:
    ly.append((w[0] * x + b) / (-1 * w[1]))

plot.figure()
plot.scatter(px, py, c='r')
plot.scatter(nx, ny, c='b')
plot.scatter(linsvm.supportx, linsvm.supporty, c='g', marker='x')
plot.plot(lx, ly)
plot.show()


nonlinData = dr.readData('nonlinsep.txt')

radialsvm = svm.RadialKernelSVM(nonlinData)
w, b = radialsvm.train()


px, py = extract(nonlinData, +1)
nx, ny = extract(nonlinData, -1)

print(w)
print(b)

correctRate = radialsvm.test(nonlinData)
print('percent correct')
print(correctRate)

plot.figure()
plot.scatter(px, py, c='r')
plot.scatter(nx, ny, c='b')
plot.scatter(radialsvm.supportx, radialsvm.supporty, c='g', marker='x')
plot.show()