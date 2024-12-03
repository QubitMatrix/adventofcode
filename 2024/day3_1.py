import re
pattern = r"mul\(\d\d?\d?,\d\d?\d?\)"
inp = ""
ans = 0
while(True):
    try:
        inp = input()
        matches = re.findall(pattern,inp)
        print(inp, matches)
        for x in matches:
            a,b = x[x.find("(")+1:x.find(")")].split(",")
            ans += int(a)*int(b)
    except Exception as e:
        print(e)
        break
print(ans)
