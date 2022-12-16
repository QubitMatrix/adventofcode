import copy
lights=[]#lights=[[0]*1000]*1000 will create rows of same address so modifying one row modifies all the rows
for x in range(1000):
    lights.append([])
    for y in range(1000):
        lights[x].append(0)
try:
 while(1):
    s=input()
    s=s.split()
    if(s[0]=="turn"):
        s=s[1:]
    r1,c1=list(map(int,s[1].split(",")))
    r2,c2=list(map(int,s[3].split(",")))
    if(s[0]=="on"):
        for x in range(r1,r2+1):
            lights[x][c1:c2+1]=[lights[x][y]+1 for y in range(c1,c2+1)]
    elif(s[0]=="off"):
        for x in range(r1,r2+1):
            lights[x][c1:c2+1]=[lights[x][y]-1 if(lights[x][y]!=0) else 0 for y in range(c1,c2+1)] 
    else:
        for x in range(r1,r2+1):
            lights[x][c1:c2+1]=[lights[x][y]+2 for y in range(c1,c2+1)]
except EOFError:
    count=0
    for x in lights:
        for y in x:
            count+=y
    print(count)
except Exception as e:
    print(e)
