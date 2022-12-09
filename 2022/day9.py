import math
tailpos=set()
head=[0,0]
tail=[0,0]
try:
    while(1):
        pos,num=input().split()
        num=int(num)
        if(pos=="R"):
            for x in range(num):
                head[1]+=1
                if(math.fabs(head[1]-tail[1])>1):
                    if(tail[0]==head[0]):#same row
                        tail[1]+=1
                    elif(head[0]>tail[0]):
                        tail[1]+=1
                        tail[0]+=1
                    else:
                        tail[1]+=1
                        tail[0]-=1
                tailpos.add(tuple(tail))
        if(pos=="L"):
            for x in range(num):
                head[1]-=1
                if(math.fabs(head[1]-tail[1])>1):
                    if(tail[0]==head[0]):#same row
                        tail[1]-=1
                    elif(head[0]>tail[0]):
                        tail[1]-=1
                        tail[0]+=1
                    else:
                        tail[1]-=1
                        tail[0]-=1
                tailpos.add(tuple(tail))
        if(pos=="U"):
            for x in range(num):
                head[0]+=1
                if(math.fabs(head[0]-tail[0])>1):
                    if(tail[1]==head[1]):#same column
                        tail[0]+=1
                    elif(head[1]>tail[1]):
                        tail[1]+=1
                        tail[0]+=1
                    else:
                        tail[1]-=1
                        tail[0]+=1
                tailpos.add(tuple(tail))
        if(pos=="D"):
            for x in range(num):
                head[0]-=1
                if(math.fabs(head[0]-tail[0])>1):
                    if(tail[1]==head[1]):#same column
                        tail[0]-=1
                    elif(head[1]>tail[1]):
                        tail[1]+=1
                        tail[0]-=1
                    else:
                        tail[1]-=1
                        tail[0]-=1
                tailpos.add(tuple(tail))


except EOFError:
    print(len(tailpos))
except Exception as e:
    print(e)


