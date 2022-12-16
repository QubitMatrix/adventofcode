dic={}
dic_arr={}
def eval(ins,key):
        input_wires=ins[key]
        if("AND" in input_wires):
            lhs=input_wires.split(" AND ")
            if(lhs[0].isnumeric()):
                dic[lhs[0]]=int(lhs[0])
            if(lhs[1].isnumeric()):
                dic[lhs[1]]=int(lhs[1])
            if(lhs[0] not in dic.keys()):
                eval(ins,lhs[0])
            if(lhs[1] not in dic.keys()):
                eval(ins,lhs[1])
            val=dic[lhs[0]] & dic[lhs[1]]
        elif("OR" in input_wires):
            lhs=input_wires.split(" OR ")
            if(lhs[0].isnumeric()):
                dic[lhs[0]]=int(lhs[0])
            if(lhs[1].isnumeric()):
                dic[lhs[1]]=int(lhs[1])
            if(lhs[0] not in dic.keys()):
                eval(ins,lhs[0])
            if(lhs[1] not in dic.keys()):
                eval(ins,lhs[1])
            val=dic[lhs[0]] | dic[lhs[1]]
        elif("NOT" in input_wires):
            lhs=input_wires[input_wires.index(' ')+1:]
            if(lhs.isnumeric()):
                dic[lhs]=int(lhs)
            if(lhs not in dic.keys()):
                eval(ins,lhs)
            val=(2**16)+~dic[lhs]
        elif("LSHIFT" in input_wires):
            lhs=input_wires.split(" LSHIFT ")
            if(lhs[0].isnumeric()):
                dic[lhs[0]]=int(lhs[0])
            if(lhs[0] not in dic.keys()):
                eval(ins,lhs[0])
            val=dic[lhs[0]]<<int(lhs[1])
        elif("RSHIFT" in input_wires):
            lhs=input_wires.split(" RSHIFT ")
            if(lhs[0].isnumeric()):
                dic[lhs[0]]=int(lhs[0])
            if(lhs[0] not in dic.keys()):
                eval(ins,lhs[0])
            val=dic[lhs[0]]>>int(lhs[1])
        else:
            try:
                val=int(input_wires)
            except Exception as e:
                if(input_wires not in dic.keys()):
                    eval(ins,input_wires)
                val=dic[input_wires]
        dic[key]=val

try:
    while(1):
        s=input()
        s=s.split(" -> ")
        dic_arr[s[1]]=s[0]
except EOFError:
    eval(dic_arr,"a")
    print("part1:",dic["a"])
    t=dic['a']
    dic={}
    dic['b']=t
    eval(dic_arr,"a")
    print("part2:",dic["a"])
    
except Exception as e:
    print(e)

