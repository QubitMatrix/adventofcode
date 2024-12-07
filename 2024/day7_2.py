import copy
ans = 0
def generate_operator_combinations(size):
    operators = ['*', '+', '||']
    num_combinations = 3 ** size  # Total combinations
    combinations = []

    for i in range(num_combinations):
        # Convert integer `i` to base-3 representation
        base3 = []
        temp = i
        while temp > 0:
            base3.append(temp % 3)
            temp //= 3
        base3 = base3[::-1]  # Reverse to get the correct order

        # Pad with leading zeros to match the size
        while len(base3) < size:
            base3.insert(0, 0)

        # Map digits to operators
        combination = [operators[digit] for digit in base3]
        combinations.append(combination)

    return combinations
def check_calibration(val, nums):
    nums = nums[::-1]
    combinations = generate_operator_combinations(len(nums)-1)
    for combination in combinations:
        nums_1 = copy.deepcopy(nums)
        for op in combination:
            a = nums_1.pop()
            b = nums_1.pop()
            if(op == '+'):
                res = (a+b)
            elif(op == '||'):
                res = int(str(a) + str(b))
            else:
                res = (a*b)
            nums_1.append(res)
            if(res > val):
                break
        if(nums_1[0] == val):
            return val
    return 0

count = 0
while(True):
    try:
        inp = input()
        val, nums = int(inp.split(": ")[0]), list(map(int,inp.split(": ")[1].split()))
        print(count)
        count += 1
        if(check_calibration(val,nums)):
            ans += val
    except Exception as e:
        print(e)
        break
print(ans)
