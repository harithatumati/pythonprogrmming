n=int(input())
k=int(input())
for m in range (n,k+1):
	if m>1:
		for i in range(2,m):
			if m%i==0:
				break
			print(m)
