try:
    while(1):
        s=input()
        arr=[]
        arr2=[]
        x1=x2=0
        for x in range(0,len(s),1):
            if(x+3<len(s) and x1==0):
                arr.extend([s[y] for y in range(x,x+4)])
                if(len(set(arr))==4):
                    print("part1",x+4)
                    x1=1
                else:
                    arr=[]
            if(x+14<len(s)and x2==0):
                arr2.extend([s[y] for y in range(x,x+14)])
                if(len(set(arr2))==14):
                    print("part2",x+14)
                    x2=1
                    break
                else:
                    arr2=[]
            else:
                break
except:
    print("EOF")
