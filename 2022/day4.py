a1=set()
a2=set()
count=0
count2=0
try:
    while(1):
        s=input()
        a1=set()
        a2=set()
        s1,s2=s.split(",")
        a,b=list(map(int,s1.split("-")))
        for x in range(a,b+1):
            a1.add(x)
        c,d=list(map(int,s2.split("-")))
        for x in range(c,d+1):
            a2.add(x)
        #part1:
        if(a1.issubset(a2) or a2.issubset(a1)):
            count+=1
        #part2:
        if(a in a2 or b in a2 or c in a1 or d in a1):
            count2+=1
except Exception as e:
    print(count,count2)
        
