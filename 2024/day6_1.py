direction = 'u'
arr = []
while(True):
    try:
        inp = input()
        arr.append(inp)
        if('^' in inp):
            col = inp.find('^')
            pos = [len(arr)-1,col]
            print(pos)
    except:
        break

print(arr)
positions = set()
positions.add(tuple(pos))
while(pos[0] > -1 and pos[0] < len(arr) and pos[1] > -1 and pos[-1] < len(arr[0])):
    if(direction == 'u'):
        if(pos[0] == 0):
            break
        if(arr[pos[0]-1][pos[1]] == '#'):
            direction = 'r'
        else:
            pos[0] -= 1
    elif(direction == 'd'):
        if(pos[0] == len(arr)-1):
            break
        if(arr[pos[0]+1][pos[1]] == '#'):
            direction = 'l'
        else:
            pos[0] += 1
    elif(direction == 'r'):
        if(pos[1] == len(arr[0])-1):
            break
        if(arr[pos[0]][pos[1]+1] == '#'):
            direction = 'd'
        else:
            pos[1] += 1
    else:
        if(pos[1] == 0):
            break
        if(arr[pos[0]][pos[1]-1] == '#'):
            direction = 'u'
        else:
            pos[1] -=1
    positions.add(tuple(pos))

print(len(positions))
