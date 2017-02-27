import pcaparser
import pca

data = pcaparser.parsedatafile('pca-data.txt')
principalComponents = pca.doPCA(data, 2)
print(principalComponents)