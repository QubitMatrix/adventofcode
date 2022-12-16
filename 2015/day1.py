floor=0
pos=0
s=input()
for x in range(len(s)):
    if(s[x]=='('):
        floor+=1
    else:
        floor-=1
    if(floor==-1 and pos==0):
        pos=x+1
print(floor,pos)
