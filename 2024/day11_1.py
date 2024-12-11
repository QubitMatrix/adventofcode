from timeit import default_timer as timer
start = timer()
inp = list(map(int, input().split()))
count = 0
while(count < 25):
    pos = 0
    while(pos < len(inp)):
        val = inp[pos]
        if(val == 0):
            inp[pos] = 1
        elif(len(str(val))%2 == 0):
            split_1 = int(str(val)[:len(str(val))//2])
            split_2 = int(str(val)[len(str(val))//2:])
            inp[pos] = split_1
            inp.append(-1)
            inp[pos+2:] = inp[pos+1:-1]
            inp[pos+1] = split_2
            pos += 1
        else:
            inp[pos] *= 2024
        pos += 1
    count += 1
    print(count)
end = timer()
print(end-start)
print(len(inp))
