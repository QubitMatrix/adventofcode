arr=[]
s3=0
try:
    while(1):
        s=input()
        s1=s[:len(s)//2]
        s2=s[len(s)//2:]
        arr=[]
        for x in s1:
            if(x in s2 and x not in arr):
                arr.append(x)
                if(x.islower()):
                    s3+=ord(x)-ord('a')+1
                else:
                    s3+=ord(x)-ord('A')+27
except:
    print(s3)

