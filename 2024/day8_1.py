import math
from collections import defaultdict
import itertools
pos = set()
row = 0
antennas = defaultdict(list)
while(True):
    try:
        row += 1
        inp = input()
        for col in range(len(inp)):
            if(inp[col] != '.'):
                antennas[inp[col]].append((row, col+1))
        col = len(inp) + 1
    except:
        break

print(antennas)
for antenna in antennas.keys():
    pairs = list(itertools.combinations(antennas[antenna],2))
    for pair in pairs:
        a = pair[0] if pair[0][0] < pair[1][0] else pair[1]
        b = pair[1] if pair[0][0] < pair[1][0] else pair[0]
        slope = (b[1] - a[1]) / (b[0] - a[0])
        print(a,b,slope)
        distance = math.fabs(a[0] - b[0])
        print(distance,row,col)
        x1 = a[0] - distance
        x2 = b[0] + distance
        y1 = a[1] - (slope * distance)
        y2 = (slope * distance) + b[1] 
        print(x1,y1)
        print(x2,y2)
        if(x1 > 0 and x1 < row and y1 > 0 and y1 < col):
            pos.add((x1,y1))
        if(x2 > 0 and x2 < row and y2 > 0 and y2 < col):
            pos.add((x2,y2))
print(len(pos))
