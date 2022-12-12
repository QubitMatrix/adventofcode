import copy
monkey=[]
ins={}
dic={"start":"","operation":"","test":""}
try:
    while(1):
        s=input()
        _,num=s.split()
        num=num[:-1]
        _,s=input().split(":")
        dic["start"]=[int(x) for x in s.split(",")]
        _,s=input().split(":")
        val=s[s.index("d")+4:]
        try:
            dic["operation"]=[s[s.index("d")+2],int(val)]
        except:
            dic["operation"]=[s[s.index("d")+2],val]
        s=input().split()
        s1=input().split()
        s2=input().split()
        dic["test"]=[int(s[-1]),int(s1[-1]),int(s2[-1])]
        monkey.append(dic)
        dic={}
        s=input()
except EOFError:
    dmonkey=copy.deepcopy(monkey)
    for x in range(20):
        for y in range(len(monkey)):
            dmonkey=copy.deepcopy(monkey)
            for z in dmonkey[y]["start"]:
                try:
                    ins[y]+=1
                except:
                    print("a")
                    ins[y]=1
                if(monkey[y]["operation"][0]=="+"):
                    try:
                        worry=(z+monkey[y]["operation"][1])//3
                    except:
                        worry=(z+z)//3
                    monkey[y]["start"].remove(z)
                    if(worry%monkey[y]["test"][0]==0):
                        monkey[monkey[y]["test"][1]]["start"].append(worry)
                    else:
                        monkey[monkey[y]["test"][2]]["start"].append(worry)
                elif(monkey[y]["operation"][0]=="*"):
                    try:
                        worry=(z*monkey[y]["operation"][1])//3
                    except:
                        worry=(z*z)//3
                    monkey[y]["start"].remove(z)
                    if(worry%monkey[y]["test"][0]==0):
                        monkey[monkey[y]["test"][1]]["start"].append(worry)
                    else:
                        monkey[monkey[y]["test"][2]]["start"].append(worry)
    ins=sorted(ins.items(),key=lambda x:x[1])
    print(ins[-2][1]*ins[-1][1])
except Exception as e:
    print(e)

