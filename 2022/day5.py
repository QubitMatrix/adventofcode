import copy
import re
stack=[]#,[],[],[],[],[],[]]
stack.append(['F','C','J','P','H','T','W'])
stack.append(['G','R','V','F','Z','J','B','H'])
stack.append(['H','P','T','R'])
stack.append(['Z','S','N','P','H','T'])
stack.append(['N','V','F','Z','H','J','C','D'])
stack.append(['P','M','G','F','W','D','Z'])
stack.append(['M','V','Z','W','S','J','D','P'])
stack.append(['N','D','S'])
stack.append(['D','Z','S','F','M'])
'''
stack.append(['Z','N'])
stack.append(['M','C','D'])
stack.append(['P'])
'''
counter=0
stack1=copy.deepcopy(stack)
count=0
counter2=0
counter3=0
try:
    while(1):
        inp=input()
        '''s=re.split('\W+',inp)
        check=inp.split(" ")
        if(check[0]!=""):
            s=s[1:]
        if(check[-1]!=""):
            s=s[:-1]
        print(s)
        counter3=0'''
        if("1" in inp):
            '''print(stack)
            for x in range(len(stack)):
                stack[x].reverse()
            #stack=stack.reverse()
            print(stack)'''
            raise SyntaxError
        '''else:
            for x in s:
                if(x!=""):
                    try:
                        stack[counter3].extend(x)
                    except:
                        stack.append([])
                        stack[counter3].extend(x)
                else:
                    try:
                        a=stack[counter3]
                    except:
                        stack.append([])
                counter3+=1'''
                
except SyntaxError:
    try:
        s=input()
        while(1):
            s=input().split()
            for x in s:
                if(x.isdigit() and counter==0):
                    count=int(x)
                    counter+=1
                elif(x.isdigit() and counter==1):
                    counter+=1
                    src=(int)(x)
                elif(x.isdigit() and counter==2):
                    counter=0
                    des=int(x)
            while(counter2<count):
                stack[des-1].append(stack[src-1][len(stack[src-1])-1])
                stack[src-1]=stack[src-1][:len(stack[src-1])-1]
                counter2+=1
            counter2=0
            stack1[des-1].extend(stack1[src-1][count*-1:])
            stack1[src-1]=stack1[src-1][:count*-1]
    except EOFError:
        s1=""
        s2=""
        for x in stack:
            s1+=x[-1]
        for x in stack1:
            s2+=x[-1]
        print(s1,s2)
except EOFError:
    print("EOF")
