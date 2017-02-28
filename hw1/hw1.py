__author__ = 'paul'
#no other partner for this homework

import nightoutparser
import id3
import nightoutdata

def constructQuery():
    return nightoutdata.Row('Large', 'Moderate', 'Cheap', 'Loud', 'City-Center', 'No', 'No', "")

OUTCOME = nightoutdata.ENJOY
rows = nightoutparser.parsefile("dt-data.txt")

node = id3.id3(rows, nightoutdata.allnontargetattributes, nightoutdata.ENJOY)

id3.visit([node])
id3.check(rows, node)

queryrow = constructQuery()
prediction = id3.getDecision(queryrow, node)
print('Prediction to enjoy was ' + prediction)
