import math
a=[]
b=[]
ans = 0
while(True):
    try:
        n1,n2 = list(map(int,input().split()))
        a.append(n1)
        b.append(n2)
    except:
        break

a.sort()
b.sort()

for x in range(len(a)):
    dif = math.fabs(a[x] - b[x])
    ans += int(dif)


print(ans)
