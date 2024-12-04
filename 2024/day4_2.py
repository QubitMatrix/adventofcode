arr = []
while(True):
    try:
        inp = input()
        arr.append(inp)
    except:
        break

ans = 0
for row in range(0, len(arr)-2,1):
    for col in range(0, len(arr[0])-2,1):
        if(arr[row][col] == 'M'):
            if((arr[row+2][col] == 'M' and arr[row][col+2] == 'S' or arr[row+2][col] == 'S' and arr[row][col+2] == 'M') and arr[row+2][col+2] == 'S' and arr[row+1][col+1] == 'A'):
                ans += 1
        elif(arr[row][col] == 'S'):
            if((arr[row+2][col] == 'M' and arr[row][col+2] == 'S' or arr[row+2][col] == 'S' and arr[row][col+2] == 'M') and arr[row+1][col+1] == 'A' and arr[row+2][col+2] == 'M'):
                ans += 1

print(ans)
