import re
def calc(s,dic):
    if(type(dic[s])==int):
        return dic[s]
    else:
        s1=""
        sym=dic[s][5]
        x,y=re.split("[+]|[-]|[/]|[*]",dic[s])
        x=x.strip()
        y=y.strip()
        if(type(dic[x])!=int):
            dic[x]=calc(x,dic)
        if(type(dic[y])!=int):
            dic[y]=calc(y,dic)
        s1=str(dic[x])+sym+str(dic[y])
        print(s1)
        return int(eval(s1))

dic={}
try:
    while(1):
        s=input()
        mon,val=s.split(": ")
        try:
            dic[mon]=int(val)
        except:
            dic[mon]=val
except:
    x=calc("root",dic)
    print(x)
