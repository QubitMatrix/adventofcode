from collections import defaultdict
a = []
b = defaultdict(int)
ans = 0
while(True):
    try:
        n1, n2 = list(map(int, input().split()))
        a.append(n1)
        b[n2] += 1
    except:
        break


for x in a:
    ans += x * b[x]

print(ans)
