def check_trail(arr,row,col,val):
    global ans
    if(val == 10):
        ans += 1
        return
    if(row > 0 and arr[row-1][col] == val):
        check_trail(arr,row-1,col,val+1)
    if(row < len(arr) - 1 and arr[row+1][col] == val):
        check_trail(arr,row+1,col,val+1)
    if(col > 0 and arr[row][col-1] == val):
        check_trail(arr,row,col-1,val+1)
    if(col < len(arr[0]) - 1 and arr[row][col+1] == val):
        check_trail(arr,row,col+1,val+1)

arr = []
while(True):
    try:
        inp = list(map(int,input()))
        arr.append(inp)
    except:
        break
res = 0
for row in range(len(arr)):
    for col in range(len(arr[0])):
        if(arr[row][col] == 0):
            ans = 0
            check_trail(arr,row,col,1)
            print(row,col,ans)
            res += ans

print(res)

