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