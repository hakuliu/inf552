__author__ = 'paul'

import nightoutparser
import id3
import nightoutdata

def visit(currentlevel):
    if(len(currentlevel)==0): return
    str = ''
    nextlevel = []
    for node in currentlevel:
        str += node.name + ','
        for branch in node.branches:
            nextlevel.append(branch)
    print(str)
    visit(nextlevel)

def check(rows, root):
    countCorrect = 0
    for row in rows:
        answer = row.attr[nightoutdata.ENJOY]
        fromTree = id3.getDecision(row, root)
        if(answer == fromTree):
            countCorrect+=1
    percentage = float(countCorrect) / len(rows)
    print('%f correct' % percentage)

def constructQuery():
    return nightoutdata.Row('Large', 'Moderate', 'Cheap', 'Loud', 'City-Center', 'No', 'No', "")

OUTCOME = nightoutdata.ENJOY
rows = nightoutparser.parsefile("dt-data.txt")
node = id3.id3(rows, nightoutdata.allnontargetattributes, 'Enjoy')
visit([node])
check(rows, node)
queryrow = constructQuery()
prediction = id3.getDecision(queryrow, node)
print('Prediction to enjoy was ' + prediction)
