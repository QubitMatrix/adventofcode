from collections import defaultdict
dic = defaultdict(set)
updates = []
while(True):
    try:
        inp1, inp2 = list(map(int, input().split("|")))
        dic[inp1].add(inp2)
    except:
        break

while(True):
    try:
        update = list(map(int, input().split(",")))
        updates.append(update)
    except:
        break

print(dic,updates)
ans = 0
for update in updates:
    flag = 0
    prev = set()
    for x in update:
        if(prev.intersection(dic[x])!=set()):
            flag = 1
            break
        prev.add(x)
    if(not flag):
        print(update)
        ans += update[len(update)//2]

print(ans)
