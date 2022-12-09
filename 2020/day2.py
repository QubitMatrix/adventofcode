count1=count2=0
try:
    while(1):
        s=input()
        x=int(s[0:s.index("-")])
        y=int(s[s.index("-")+1:s.index(" ")])
        let=s[s.index(" ")+1]
        string=s[s.index(":")+2:]
        count=string.count(let)
        #part1:
        if(count>=x and count<=y):
            count1+=1
        #part2:
        if((string[x-1]==let)^(string[y-1]==let)):
            count2+=1
except EOFError:
    print(count1,count2)
except Exception as e:
    print(e)
