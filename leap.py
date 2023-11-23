Printing count of leap years in the given range

Program:
def leap(yr):
    if yr%400==0:
        return True
    elif yr%4==0 and yr%100!=0:
        return True
    else:
        return False
s,e=map(int,input().split())
l=[i for i in range (s,e+1) if leap(i)]
print(len(l))

Output:
2000 2010
3
