a=[]
arr=[]
tot=""
sum1=0
try:
    while(1):
        count=0
        a=[]
        item=0
        tot=""
        arr=[]
        while(count<3):
            s=input()
            s1=input()
            s2=input()
            count=3
            m=min((s1,s2,s),key=len)
            a.extend([s,s1,s2])
            a.remove(m)
            n,o=a
            tot=s+s1+s2
            for x in range(len(m)):
                if(m[x] in n and m[x] in o and m[x] not in arr):
                    if(m[x].islower()):
                        item+=ord(m[x])-ord('a')+1
                    if(m[x].isupper()):
                        item+=ord(m[x])-ord('A')+27
                    arr.append(m[x])
            sum1+=item
except Exception as e:
    print(sum1)
                
        
