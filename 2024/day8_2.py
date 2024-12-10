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

for antenna in antennas.keys():
    pairs = list(itertools.combinations(antennas[antenna],2))
    for pair in pairs:
        a = pair[0] if pair[0][0] < pair[1][0] else pair[1]
        b = pair[1] if pair[0][0] < pair[1][0] else pair[0]
        if(a[0] == b[0]):
            print("r")
        if(a[1] == b[1]):
            print("c")
        #print(a,b,slope)
        slope = (b[1] - a[1]) / (b[0] - a[0])
        distance = -1
        flag1 = 0
        flag2 = 0
        while((not flag1) or (not flag2)):
            distance += 1
            #print(distance,row,col)
            x1 = round(a[0] - distance,3)
            x2 = round(b[0] + distance,3)
            y1 = round(a[1] - (slope * distance),3)
            y2 = round((slope * distance) + b[1],3) 
            #print(x1,y1)
            #print(x2,y2)
            if(x1 > 0 and x1 < row and y1 > 0 and y1 < col):
                if(int(y1) == y1):
                    pos.add((x1,int(y1)))
            else:
                flag1 = 1
            if(x2 > 0 and x2 < row and y2 > 0 and y2 < col):
                if(int(y2) == y2):
                    pos.add((x2,int(y2)))
            else:
                flag2 = 1
        distance = b[0] - a[0]
        while(distance > 0):
            distance -= 1
            x1 = a[0] + distance
            y1 = (slope * distance) + a[1] 
            if(x1 > 0 and x1 < row and y1 > 0 and y1 < col):
                if(int(x1) == x1 and int(y1) == y1):
                    pos.add((x1,int(y1)))

print(len(pos))
