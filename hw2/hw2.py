#programmed entirely by Paul An

import clusterparser
import kmeans

#for testing and visualization
def writeKAssignments(assignments):
    f = open('test.csv', 'w')
    for assignment in assignments:
        f.write(str(assignment) + '\n')
    f.close()

points = clusterparser.parsedatafile("clusters.txt")
centroids, assignments = kmeans.kmeans(points, 3)
print(centroids)


