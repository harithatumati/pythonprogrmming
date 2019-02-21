n,m=map(int,input().split())
temp=n
n=m
m=temp
e=[]
e.append(n)
e.append(temp)
h=' '.join(map(str,e))
print(h)

