def get_region(arr, row, col, val):
    global visited
    global area
    global perimeter
    print(row,col)
    visited.add((row,col))
    area += 1
    if(row < len(arr) - 1 and arr[row+1][col] == val and (row+1,col) not in visited):
        get_region(arr, row+1,col,val)
    elif(row >= len(arr) - 1 or arr[row+1][col] != val):
        print(row,col)
        perimeter += 1
    if(row > 0 and arr[row-1][col] == val and (row-1,col) not in visited):
        get_region(arr, row-1,col,val)
    elif(row <= 0 or arr[row-1][col] != val):
        print(row,col)
        perimeter += 1
    if(col < len(arr[0]) - 1 and arr[row][col+1] == val and (row,col+1) not in visited):
        get_region(arr, row,col+1,val)
    elif(col >= len(arr[0]) - 1 or arr[row][col+1] != val):
        print(row,col)
        perimeter += 1
    if(col > 0 and arr[row][col-1] == val and (row,col-1) not in visited):
        get_region(arr, row,col-1,val)
    elif(col <= 0 or arr[row][col-1] != val):
        print(row,col)
        perimeter += 1

arr = []
while(True):
    try:
        inp = list(input())
        arr.append(inp)
    except:
        break
visited = set()
res = 0
for row in range(len(arr)):
    for col in range(len(arr[0])):
        if((row,col) not in visited):
            area = 0
            perimeter = 0
            get_region(arr, row,col,arr[row][col]) 
            print(arr[row][col],area,perimeter)
            res += area * perimeter

print(res)
