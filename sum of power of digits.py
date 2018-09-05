num=int(raw_input())
temp=num
sum=0
while temp>0:
  var=temp%10
  sum=sum+var**3
  temp/=10
if(sum==num):
   print('yes')
else:
    print('no')
