from timeit import default_timer as timer
import multiprocessing
def worker1(subarr):
    res = []
    for val in subarr:
        if(val == 0):
            ans = [1]
        elif(len(str(val))%2 == 0):
            split_1 = int(str(val)[:len(str(val))//2])
            split_2 = int(str(val)[len(str(val))//2:])
            ans = [split_1,split_2]
        else:
            ans = [val*2024]
        res.extend(ans)
    return res

start = timer()
inp = list(map(int, input().split()))
count = 0
while(count < 25):
    num_workers = multiprocessing.cpu_count()
    subarr_size = len(inp) // num_workers
    subarrs = [inp[start:start+subarr_size] for start in range(0,len(inp),subarr_size)]
    with multiprocessing.Pool(num_workers) as pool:
        results = pool.map(worker1, subarrs)
    inp = [val for result in results for val in result] 
    count += 1
    print(count)
end = timer()
print(end-start)
print(len(inp))
