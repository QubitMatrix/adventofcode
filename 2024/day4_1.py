import re
arr = []
pattern1 = r"XMAS"
pattern2 = r"SAMX"
ans = 0
while(True):
    try:
        inp = input()
        count1 = len(re.findall(pattern1,inp))
        count2 = len(re.findall(pattern2,inp))
        ans += count1 + count2
        print(count1,count2)
        arr.append(inp)
    except:
        break

print(arr,ans)
cols = []
for col in range(len(arr[0])):
    val = ""
    for row in range(len(arr)):
        val += arr[row][col]
    count1 = len(re.findall(pattern1,val))
    count2 = len(re.findall(pattern2,val))
    ans += count1 + count2
    print(count1,count2)
    cols.append(val)

print(cols,ans)

diagonals_left = []
for start_col in range(len(arr[0])-len(pattern1)+1):
    row = 0
    col = start_col
    val = ""
    while(row < len(arr) and col < len(arr[0])):
        val += arr[row][col]
        row += 1
        col += 1
    diagonals_left.append(val)
    count1 = len(re.findall(pattern1,val))
    count2 = len(re.findall(pattern2,val))
    ans += count1 + count2
    print(count1,count2)
for start_col in range(len(arr[0])-2, len(pattern1)-2, -1):
    row = len(arr)-1
    col = start_col
    val = ""
    while(row > 0 and col > -1):
        val += arr[row][col]
        row -= 1
        col -= 1
    diagonals_left.append(val)
    count1 = len(re.findall(pattern1,val))
    count2 = len(re.findall(pattern2,val))
    ans += count1 + count2
    print(count1,count2)
print(diagonals_left,ans)

diagonals_right = []
for start_col in range(len(arr[0])-1, len(pattern1)-2,-1):
    row = 0
    col = start_col
    val = ""
    while(row < len(arr) and col > -1):
        val += arr[row][col]
        row += 1
        col -= 1
    val = val[::-1]
    diagonals_right.append(val)
    count1 = len(re.findall(pattern1,val))
    count2 = len(re.findall(pattern2,val))
    ans += count1 + count2
    print(count1,count2)
for start_col in range(1, len(arr[0])-len(pattern1)+1, 1):
    row = len(arr)-1
    col = start_col
    val = ""
    while(row > 0 and col < len(arr[0])):
        val += arr[row][col]
        row -= 1
        col += 1
    val = val[::-1]
    diagonals_right.append(val)
    count1 = len(re.findall(pattern1,val))
    count2 = len(re.findall(pattern2,val))
    ans += count1 + count2
    print(count1,count2)

print(diagonals_right,ans)
print(ans)
