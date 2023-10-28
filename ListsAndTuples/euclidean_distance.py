import math

def calcDist(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

plotData = [[1,2],[2,6],[3,4],[-1,-4],[-2,4]]

maxset = []
maxdist = -1

for pd1 in plotData:
    for pd2 in plotData:
        dist = calcDist(pd1,pd2)
        print(pd1,"to",pd2,":",dist)
        if dist > maxdist:
            maxdist = dist
            maxset = [pd1,pd2]

print("\nMax distance set: ", maxset)
print("Distance: ",maxdist)
