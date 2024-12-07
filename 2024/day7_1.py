import copy
ans = 0
def check_calibration(val, nums):
    nums = nums[::-1]
    bitmask = []
    for x in range(2**(len(nums)-1)):
        masks = []
        for y in range(len(nums)-1):
            if(x & 1<<y):
                masks.append('+')
            else:
                masks.append('*')
        bitmask.append(masks)
    print(bitmask)
    for combination in bitmask:
        nums_1 = copy.deepcopy(nums)
        print(nums,nums_1)
        for op in combination:
            a = nums_1.pop()
            b = nums_1.pop()
            if(op == '+'):
                res = (a+b)
            else:
                res = (a*b)
            nums_1.append(res)
            if(res > val):
                break
        if(nums_1[0] == val):
            return val
    return 0

while(True):
    try:
        inp = input()
        val, nums = int(inp.split(": ")[0]), list(map(int,inp.split(": ")[1].split()))
        print(val, nums)
        if(check_calibration(val,nums)):
            ans += val
    except Exception as e:
        print(e)
        break
print(ans)
