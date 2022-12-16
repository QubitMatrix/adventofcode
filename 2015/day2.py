area=0
tot_area=0
tot_ribbon=0
try:
    while(1):
        s=input()
        s=s.split("x")
        s=list(map(int,s))
        print(s)
        ar1=s[0]*s[1]
        ar2=s[1]*s[2]
        ar3=s[0]*s[2]
        area=2*(ar1+ar2+ar3)+min(ar1,ar2,ar3)
        tot_area+=area
        s.sort()
        print(s)
        perimeter_min=2*sum(s[0:2])
        ribbon=s[0]*s[1]*s[2]+perimeter_min
        tot_ribbon+=ribbon
except EOFError:
    print(tot_area,tot_ribbon)
except Exception as e:
    print(e)
