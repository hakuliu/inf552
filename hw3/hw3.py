import pcaparser
import pca
import fastmapparser
from fastmap import FastMapper

data = pcaparser.parsedatafile('pca-data.txt')
principalComponents = pca.doPCA(data, 2)
print(principalComponents)

O = fastmapparser.parsefile('fastmap-data.txt')
mapper = FastMapper(O)
mapper.fastMap(2)
mapper.writeFile('fastmap-out.csv')
images = mapper.images
words = fastmapparser.parsewords('fastmap-wordlist.txt')

import pylab
pylab.scatter([x[0] for x in images], [x[1] for x in images], c="r")
for i,s in enumerate(words):
    pylab.annotate(s,images[i])

pylab.title("Levenshtein distance mapped to 2D coordinates")
pylab.show()