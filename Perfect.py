t=int(input())
for i in range(t):
  n=int(input())
  t=n
  s=0
  for i in range(1,n):
    if(n%1==0):
      s=s+i
      if(s==t):
        print("Perfect number")
      else:
        print('Not perfect number')
