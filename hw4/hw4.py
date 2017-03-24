import numpy
import linreg
from perceptron import Perceptron
from pocketperceptron import PocketPerceptron
from logitreg import LogisticRegression

######################PERCEPTRON
'''
perc = Perceptron(3)
for line in open('classification.txt', 'r'):
    line = line.split(',')
    row = [float(line[0]), float(line[1]), float(line[2])]
    val = int(line[3])
    perc.digest(row, val)

print('perceptron weights are:')
print(perc.weights)

correct = 0
total = 0
for line in open('classification.txt', 'r'):
    line = line.split(',')
    row = [float(line[0]), float(line[1]), float(line[2])]
    val = int(line[3])
    prediction = perc.predict(row)
    total += 1
    if val == prediction:
        correct += 1

print('perceptron error: ')
error = 1 - float(correct) / total
print(error)
'''
#########################POCKET PERCEPTRON
'''
perc = PocketPerceptron(3)
allrows = []
allvals = []
for line in open('classification.txt', 'r'):
    line = line.split(',')
    row = [float(line[0]), float(line[1]), float(line[2])]
    val = int(line[4])
    allrows.append(row)
    allvals.append(val)

for i in range(7000):
    perc.digest(allrows, allvals)
perc.finalize()
print('pocket perceptron weights are:')
print(perc.weights)


correct = 0
total = 0
for i in range(len(allvals)):
    row = allrows[i]
    val = allvals[i]
    prediction = perc.predict(row)
    total += 1
    if val == prediction:
        correct += 1

print('pocket perceptron error: ')
error = 1 - float(correct) / total
print(error)
'''
#######################LOGIT

perc = LogisticRegression(3)
allrows = []
allvals = []
for line in open('classification.txt', 'r'):
    line = line.split(',')
    row = [float(line[0]), float(line[1]), float(line[2])]
    val = int(line[4])
    allrows.append(row)
    allvals.append(val)

for i in range(7000):
    perc.digest(allrows, allvals)
print('logistic regression weights are:')
print(perc.weights)

countcorrect = 0
for i in range(len(allvals)):
    val = allvals[i]
    row = allrows[i]
    p = perc.predict(row)
    #just a mock for now
    prediction = 1
    if(p < .5):
        prediction = -1
    if(prediction == val):
        countcorrect += 1
error = 1 - float(countcorrect) / len(allvals)
print('error for logit:')
print(error)

#######################LINEAR REGRESSION
'''
x = []
y = []
for line in open('linear-regression.txt', 'r'):
    line = line.split(',')
    row = [1,float(line[0]), float(line[1])]
    val = float(line[2])
    x.append(row)
    y.append([val])
x = numpy.transpose(x)
w = linreg.getW(x, y)
print('linear regression weights:')
print w

'''