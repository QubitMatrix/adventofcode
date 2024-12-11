from collections import defaultdict
def step_stones(stones):
    stones_n = defaultdict(int)
    for stone, count in stones.items():
        if(stone == 0):
            stones_n[1] += count
        elif(len(str(stone))%2 == 0):
            stones_n[int(str(stone)[:len(str(stone))//2])] += count
            stones_n[int(str(stone)[len(str(stone))//2:])] += count
        else:
            stones_n[stone*2024] += count
    return stones_n

inp = list(map(int,input().split()))
stones = defaultdict(int)
for x in inp:
    stones[x] += 1

count = 0
while(count < 75):
    stones = step_stones(stones)
    count += 1

print(sum(stones.values()))
