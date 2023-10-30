amount=int(input())
tt=0
fh=0
th=0
oh=0
ft=0
twenty=0
ten=0
five=0
two=0
one=0
while(amount>=2000):
  tt=tt+1
  amount=amount-2000
while(amount>=500):
  tt=tt+1
  amount=amount-500
while(amount>=200):
  tt=tt+1
  amount=amount-200
  while(amount>=100):
  tt=tt+1
  amount=amount-100
  while(amount>=50):
  tt=tt+1
  amount=amount-50
  while(amount>=20):
  tt=tt+1
  amount=amount-20
  while(amount>=10):
  tt=tt+1
  amount=amount-10
  while(amount>=5):
  tt=tt+1
  amount=amount-5
  if tt>0:
    print('2000:'+str(tt))
  if fh>0:
    print('500:'+str(tt))
  if th>0:
    print('200:'+str(tt))
    if oh>0:
          print('100:'+str(tt))
      if ft>0:
            print('50:'+str(tt))
if twenty>0:
      print('20:'+str(tt))
  if ten>0:
        print('10:'+str(tt))
    if five>0:
    print('5:'+str(tt))
      if two>0:
            print('2:'+str(tt))
        if one>0:
              print('1:'+str(tt))



