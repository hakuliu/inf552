#programmed entirely by Paul An

import clusterparser
import kmeans
import em

#for testing and visualization
def writeKAssignments(assignments):
    f = open('test.csv', 'w')
    for assignment in assignments:
        f.write(str(assignment) + '\n')
    f.close()

def writeEMAssignments(assignments):
    f = open('test.csv', 'w')
    for assignment in assignments:
        f.write(str(assignment.getAssignment()) + '\n')
    f.close()

points = clusterparser.parsedatafile("clusters.txt")
centroids, kmassignments = kmeans.kmeans(points, 3)
print(centroids)
gausses, emassignments = em.em(points, 3)
for gauss in gausses:
    print(gauss.mean)

print('done')
