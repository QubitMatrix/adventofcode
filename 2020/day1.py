b=0
arr=[]
a=0
try:
    while(1):
        s=int(input())
        arr.append(s)
except Exception as e:
    for x in range(len(arr)):
        for y in range(x+1,len(arr)):
            if(arr[x]+arr[y]==2020 and a!=1):
                print(arr[x]*arr[y])
                a=1
                break
            for z in range(y,len(arr)):
                if(arr[x]+arr[y]+arr[z]==2020 and b!=1):
                    print(arr[x]*arr[y]*arr[z])
                    b=1
                    break
        if(a==1 and b==1):
            break
