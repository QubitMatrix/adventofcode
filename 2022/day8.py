count=0
arr=[]
score=[]
view_dis_up=view_dis_down=view_dis_left=view_dis_right=0
try:
    while(1):
        s=input()
        arr.append(list(map(int,s)))
except Exception as e:
    vis=2*len(arr)+2*(len(arr[0])-2)
    for x in range(1,len(arr)-1):
        for y in range(1,len(arr[0])-1):
            for z in range(x-1,-1,-1):#checking from edge to x is wrong for part2 check from x to edge
                view_dis_up+=1
                if(arr[x][y]<=arr[z][y]):
                    count+=1
                    break
            for z in range(x+1,len(arr)):
                view_dis_down+=1
                if(arr[x][y]<=arr[z][y]):
                    count+=1
                    break
            for z in range(y-1,-1,-1):
                view_dis_left+=1
                if(arr[x][y]<=arr[x][z]):
                    count+=1
                    break
            for z in range(y+1,len(arr[0])):
                view_dis_right+=1
                if(arr[x][y]<=arr[x][z]):
                    count+=1
                    break
            if(count!=4):
                    scenic_score=view_dis_up*view_dis_down*view_dis_left*view_dis_right
                    score.append(scenic_score)
                    vis+=1
            count=0
            view_dis_up=view_dis_down=view_dis_left=view_dis_right=0
    print("part1",vis)
    print("part2",max(score))
