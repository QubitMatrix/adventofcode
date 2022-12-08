bre=0
dirs=[]
dic_dir={}
dic_siz={}
parent="root"
try:
   while(1):
    if(bre==0):
        s=input()
    bre=0
    if (s[2:4]=="cd"):
        dir1=s[5:]
        if(dir1==".."):
            if(len(dirs)!=1):
                dirs.pop()
        else:
            if(len(dirs)!=0):
                parent=dirs[-1]
            string=parent+"="+dir1
            dirs.append(string)
            
    elif(s[2:4]=="ls"):
        while(1):
            s=input()
            if(s[0]=="$"):
                bre=1
                break
            s1=s.split()
            if(s1[0].isnumeric()):
                for x in dirs:
                    if(x in dic_siz.keys()):
                        dic_siz[x]+=int(s1[0])
                    else:
                        dic_siz[x]=int(s1[0])
            else:
                for x in dirs:
                    if(x in dic_dir.keys()):
                        dic_dir[x].append(s1[1])
                    else:
                        dic_dir[x]=[]
                        dic_dir[x].append(s1[1])
except:
    sum1=0
    for x in dic_siz.values():
        if(x<=100000):
            sum1+=x
    print("part1",sum1)
    available=70000000-dic_siz['root=/']
    req=30000000-available
    arr=list(dic_siz.values())
    arr.sort()
    for x in arr:
        if(x>=req):
            print("part2",x)
            break

