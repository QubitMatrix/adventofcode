vowels=['a','e','i','o','u']
illegal=['ab','cd','pq','xy']
count=count2=0
def count_vowels(s):
    vow=0
    for x in s:
        if(x in vowels):
            vow+=1
    return vow
def check_double(s):
    for x in range(0,len(s)-1):
        if(s[x]==s[x+1]):
            return True
    return False
def check_double_pair(s):
    for x in range(0,len(s)-2):
        if(s[x]+s[x+1] in s[x+2:]):
            return True
    return False
def check_between(s):
    for x in range(0,len(s)-2):
        if(s[x]==s[x+2]):
            return True
    return False  

def has_illegal(s):
    for x in range(0,len(s)-1):
        if(s[x]+s[x+1] in illegal):
            return True 
    return False
try:
    while(1):
        s=input()
        count_vow=count_vowels(s)
        """PART 1:
        if(count_vow<3):
            continue
        if(not check_double(s)):
            continue
        if(not has_illegal(s)):
            print(s)
            count+=1"""
        #PART 2:
        if(not check_double_pair(s)):
            continue
        if(check_between(s)):
            count2+=1
except EOFError:
    print(count,count2)
except Exception as e:
    print(e)

