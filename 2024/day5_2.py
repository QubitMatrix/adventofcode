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
    print(update)
    pos = 0
    while(pos < len(update)):
        mov = prev.intersection(dic[update[pos]])
        if(mov!=set()):
            flag = 1
            update[pos-len(mov)] = update[pos]
            update[pos-len(mov)+1:pos+1] = mov
            pos = pos - len(mov)
            prev = prev - mov
            print("a",update)
        prev.add(update[pos])
        pos += 1
    print(update)
    if(flag):
        ans += update[len(update)//2]
print(ans)
