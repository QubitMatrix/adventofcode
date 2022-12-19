times=1
s=""
num=1113222113
count=0
while(count<50):
    s=""
    times=1
    arr=list(map(int,str(num)))
    for x in range(1,len(arr)):
        if(arr[x-1]==arr[x]):
            times+=1
        else:
            s+=str(times)+str(arr[x-1])
            times=1
    s+=str(times)+str(arr[-1])
    count+=1
    if(count==40):
        print("part1",len(s))
    num=int(s)
print("part2",len(s)) 


