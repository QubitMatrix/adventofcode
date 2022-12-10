reg=1
arr=[]
cycle=0
try:
    while(1):
        s=input()
        if(s=="noop"):
            cycle+=1
            arr.append(reg)
        else:
            _,val=s.split()
            val=int(val)
            arr.append(reg)
            arr.append(reg)
            reg=reg+val
except EOFError:
    arr.append(reg)
    signal_strength=[(x+1)*arr[x] for x in range(19,221,40)]
    print(sum(signal_strength))
    cycle=0
    crt=""
    for x in range(6):
        for y in range(40):
            if(y in range(arr[x*40+y]-1,arr[x*40+y]+2)):
                crt+="#"
            else:
                crt+="."
        crt+="\n"
    print(crt)
except Exception as e:
    print(e)
