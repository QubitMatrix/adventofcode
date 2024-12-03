ans = 0
while(True):
    try:
        report = list(map(int, input().split()))
        asc = True if report [0] < report[1] else False
        prev = report[0]
        flag = 0
        for x in report[1:]:
            if (not (asc and x - prev >= 1 and x - prev <= 3) and not(not asc and prev - x >=1 and prev - x <= 3)):
                flag = 1
                break
            prev = x
        if(not flag):
            ans += 1
    except:
        break

print(ans)
