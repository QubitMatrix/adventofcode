from collections import defaultdict
disk = input()
filesystem = []
block_details = dict()
free_pos_size = defaultdict(list)
count = 0
for x in range(0,len(disk)-1,2):
    block_details[count] = (len(filesystem), int(disk[x]))
    filesystem.extend([count]*int(disk[x]))
    filesystem.extend(['.']*int(disk[x+1]))
    free_pos_size[int(disk[x+1])].append(len(filesystem)-int(disk[x+1]))
    count += 1
block_details[count] = (len(filesystem), int(disk[-1]))
filesystem.extend([count]*int(disk[-1]))

file_id = count

while(file_id > -1):
    file_size = block_details[file_id][1]
    file_start = block_details[file_id][0]
    temp = file_size
    flag = 1
    while(temp <= max(free_pos_size.keys())):
        if(temp in free_pos_size and (flag or free_pos_size[temp][0] < free_pos_size[chosen_size][0])):
            chosen_size = temp
            flag = 0
        temp+= 1
    temp = chosen_size
    if(temp > max(free_pos_size.keys())):
        file_id -= 1
        continue
    start = free_pos_size[temp][0]
    end = free_pos_size[temp][0]+file_size
    if(start > file_start):
        file_id -= 1
        continue
    filesystem[start:end] = [file_id]*file_size
    filesystem[file_start:file_start+file_size] = ['.']*file_size
    if(temp != file_size):
        free_pos_size[temp-file_size].append(file_size+free_pos_size[temp][0])
        free_pos_size[temp-file_size].sort()
    try:
        free_pos_size[temp] = free_pos_size[temp][1:]
        if(free_pos_size[temp] == []):
            del free_pos_size[temp]
    except:
        del free_pos_size[temp]
    file_id -= 1


ans = 0
for x in range(0,len(filesystem),1):
    if(filesystem[x] != '.'):
        ans += x * filesystem[x]

print(ans)
