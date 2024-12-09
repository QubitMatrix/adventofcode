disk = input()
filesystem = []
pos = []
count = 0
for x in range(0,len(disk)-1,2):
    filesystem.extend([count]*int(disk[x]))
    filesystem.extend(['.']*int(disk[x+1]))
    pos.extend(range(len(filesystem)-int(disk[x+1]),len(filesystem),1))
    count += 1
filesystem.extend([count]*int(disk[-1]))

blank = 0
count = len(filesystem)-1
while(blank < len(pos)):
    while (filesystem[count] == '.'):
        count -= 1
    if(count < pos[blank]):
        break
    filesystem[pos[blank]] = filesystem[count]
    filesystem[count] = '.'
    blank += 1
    count -= 1

ans = 0
for x in range(0,filesystem.index('.'),1):
    ans += x * filesystem[x]

print(ans)
