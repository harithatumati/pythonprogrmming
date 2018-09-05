n=int(raw_input())
temp=n
sum=0
while temp>0:
  d=temp%10
  sum=sum+d**3
  temp/=10
if(sum==n):
   print('yes')
else:
    print('no')
