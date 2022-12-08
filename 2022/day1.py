arr=[]
sum1=0
count=1
maxx=0
maxelf=1
try:
        while(1):
            try:
                sum1+=int(input())
            except ValueError:
                arr.append(sum1)
                if(sum1>maxx):
                    maxx=sum1
                    maxelf=count
                count+=1
                sum1=0
except EOFError:
    arr.append(sum1)
    arr.sort(reverse=True)
    print(arr[0],sum(arr[:3]))

