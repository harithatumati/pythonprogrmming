n=raw_input()
a=[]
for i in range (0,n):
	a.append(input())
k=int(input())
sum=0
for i in range(0,k):
	sum=sum+a[i]
	k=a[i-1]
print(sum)
