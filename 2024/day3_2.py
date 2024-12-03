import re
pattern1 = r"mul\(\d\d?\d?,\d\d?\d?\)"
pattern2 = r"don\'t\(\)"
pattern3 = r"do\(\)"
pattern = re.compile("|".join([pattern1,pattern2,pattern3]))
inp = ""
ans = 0
flag= 1
while(True):
    try:
        inp = input()
        matches = re.findall(pattern,inp)
        print(inp, matches)
        for x in matches:
            if(x == "do()"):
                flag = 1
            elif(x == "don't()"):
                flag = 0
            elif(flag):
                a,b = x[x.find("(")+1:x.find(")")].split(",")
                print(a,b)
                ans += int(a)*int(b)
    except Exception as e:
        print(e)
        break
print(ans)
