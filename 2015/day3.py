s=input()
dic={'<':[0,-1],'>':[0,1],'v':[-1,0],'^':[1,0]}
row=col=0
row_r=col_r=0
vis_r=[]
vis=[(row,col)]
for x in range(0,len(s),2):
    row+=dic[s[x]][0]
    col+=dic[s[x]][1]
    row_r+=dic[s[x+1]][0]
    col_r+=dic[s[x+1]][1]
    if((row,col) not in vis and (row,col) not in vis_r):
        vis.append((row,col))
    if((row_r,col_r) not in vis and (row_r,col_r) not in vis_r):
        vis_r.append((row_r,col_r))
print("part1",len(vis))
print("part2",len(vis)+len(vis_r))
